#!/usr/bin/env python

#   rotation_tools 
#
#   rotation_tools is free software to analyze and synthetize rotation representations.
#  
import numpy as np
import numpy.linalg
import scipy.linalg

rotmat_header = '''
rotation matrix representation
---------------------------------
R    : rotation matrix = 
'''

angleaxis_header = '''
angle-axis rotation representation
----------------------------------
'''

def write_rotation_rep(fn, rot, angle, axis):
    angle = np.array([angle])
    degs = rads_2_degs(angle)
    axis = axis.reshape(-1,3)

    rot = rot.reshape(-1, 3)
    with open(fn, 'w') as f:
        f.write(rotmat_header)
        if rot is not None:
            np.savetxt(f, rot, '%f %f %f')
        if axis is not None:
            f.write(angleaxis_header)
            f.write('theta (rads)   : ')
            np.savetxt(f, angle, '%f')
            f.write('theta (degrees): ')
            np.savetxt(f, degs, '%f')
            f.write('w (unit vector): ')
            np.savetxt(f, axis, '%f %f %f')

def rads_2_degs(rads):
    return (180.0 / np.pi) * rads

def degs_2_rads(degs):
    return (np.pi / 180.0) * degs

def cross_product_matrix(a):
        K = np.array([  
                    [  0.0,-a[2],  a[1] ],
                    [ a[2],  0.0, -a[0] ],
                    [-a[1], a[0],   0.0 ] ])
        return K

def expmat(theta, axis): 
    """

    Exponential map from so(3) to SO(3)
    scipy implementation expm3 (used for reference, seems to work)

    """
    naxis = axis / np.linalg.norm(axis)

    Kxa = np.cross( np.eye(3) , naxis*theta)

    return scipy.linalg.expm3(Kxa)


def angle_and_axis_2_rotmat(theta, axis):
    """

    Exponential map from so(3) to SO(3)    
    https://en.wikipedia.org/wiki/Axis-angle_representation

    I = np.identity(3)
    K = cross_product_matrix(axis)
    R = I + np.sin(theta) * K + (1 - np.cos(theta)) * K^2  tochek: np.square(K)

    """
    R = expmat(theta, axis)

    return R

def rotmat_2_angle_and_axis(R):
    """

    Log map from SO(3) to so(3)
    https://en.wikipedia.org/wiki/Axis-angle_representation

    """
    theta = np.arccos( (np.trace(R)-1.0) / 2.0 )
    # dRRT is the difference between R and R^t 
    # i.e. [R-R^2] = K -> w=[k0 k1 k2]
    # R is rotation matrix
    # R^T is transponse of rotation
    # K = skew matrix or cross product matrix of vector w
    # (w is the axis vector aka 'e' rotation vector)
    dRRT = np.array([+R[2,1]-R[1,2],
                    +R[0,2]-R[2,0],
                    +R[1,0]-R[0,1]])
    axis = (1.0/(2.0*np.sin(theta))) * dRRT      
    return (theta, axis)


def angle_and_axis_to_rvec(theta, axis):
    """

    exponential rotation representation: theta*e

    theta is the angle in radians

    axis is the rotation vector 'e'

    check if R is a valid rotation matrix
    
    """
    return theta*axis


def check_rotmat(R):
    """

    check if R is a valid rotation matrix

    """
    isValid = True
    
    if np.abs(np.linalg.det(R)-1.0) > 0.000000000001:
    
        print("   WARNING: invalid rotation matrix: det != 1")
        print(np.linalg.det(R))
    
        isValid = False
    
    Rt = R.transpose()
    
    Ri = np.linalg.inv(R)
    
    if (Rt!=Ri).all(): #Rt is not Ri:
    
        print("   WARNING: invalid rotation matrix: R^-1 != R^t!")
        print(Rt)
        print(Ri)
    
        isValid = False

    return isValid 

def load_rotation_matrix(testNo):
    print ('loading test matrix ...')

    if testNo == 0:
        """
        test matrix 0:

        heading is + 30 degrees about the z axis.
        cos(heading) =  0.866  sin(heading) = 0.5      0
       -sin(heading) = -0.5    cos(heading) = 0.866    0
                        0                     0        1
        """
        R = np.array([  [ 0.86602540378443871,  0.49999999999999999,  0.00000000],
                        [-0.49999999999999999,  0.86602540378443871,  0.00000000], 
                        [ 0.00000000000000000,  0.00000000000000000,  1.00000000]])
    
    elif testNo == 1:
        # rotation of about -74 degrees around axis (-1/3,2/3,2/3)
        R = np.array([  [ 0.36000000,  0.48000000, -0.80000000],
                        [-0.80000000,  0.60000000,  0.00000000], 
                        [ 0.48000000,  0.64000000,  0.60000000]])

        print "ERROR: test matrix not supported!"

    valid = check_rotmat(R)

    if valid is not True:
        print("   WARNING: R is not a valid rotation matrix!")

    return R    

def output_rotation_representation(R, theta, axis, offsetAngleInDegs):
    """
        increment the rotation angle and regenerate the matrix with new
        angle offset
 
        output the rotation matrix, angle and axis of rotation represented
        by the matrix

    """
    print ""
 
    if offsetAngleInDegs != 0.0:
        theta = degs_2_rads(rads_2_degs(theta) + offsetAngleInDegs) 
 
        R = angle_and_axis_2_rotmat(theta, axis)
 
        print 'add %0.2f degrees to the rotation angle' % (offsetAngleInDegs)

    print 'rotation matrix R:'
    print(R) 

    # save rotation representation into a text file
    out_fn = 'rotrep.%d.txt' % (offsetAngleInDegs)

    write_rotation_rep(out_fn, R, theta, axis)

    print 'representation saved to file %s.' % out_fn


if __name__ == '__main__':

    R = load_rotation_matrix(0)

    check_rotmat(R)

    """
    test rotation matrix angular increments

    test creation of various rotation matrices that representation
    increments of 1,2,5,10 degrees respectively from the original 
    rotation matrix R.

    method.
        step 1, extract angle and axis of rotation from matrix

        step 2, increament angle of rotation

        step 3, regenerate rotation matrix from axis and incremented angle

    """
    (theta, axis) = rotmat_2_angle_and_axis(R)
    output_rotation_representation(R, theta, axis,-1.0)
    output_rotation_representation(R, theta, axis, 0.0)
    output_rotation_representation(R, theta, axis, 1.0)
    output_rotation_representation(R, theta, axis, 2.0)
    output_rotation_representation(R, theta, axis, 3.0)



  