import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

def plot_rot_mat_by_col(ax, R):
    colors = [(0.5, 0.0, 0.0), (0.05, 0.2, 0.0), (0.0, 0.0, 0.3)]
    # col1
    lines = ax.plot([0,R[0,0]],[0,R[1,0]],[0,R[2,0]]) # col1
    plt.setp(lines, color=colors[0], linewidth=2.0)

    lines = ax.plot([0,R[0,1]],[0,R[1,1]],[0,R[2,1]]) # col2
    plt.setp(lines, color=colors[1], linewidth=2.0)

    lines = ax.plot([0,R[0,2]],[0,R[1,2]],[0,R[2,2]]) # col3
    plt.setp(lines, color=colors[2], linewidth=2.0)

def plot_angle_axis(ax, theta, w):
    colors = [(1.0, 1.0, 0.1), (0.05, 1.0, 1.0), (0.0, 0.0, 0.0)]
    # col1
    lines = ax.plot([0,w[0]],[0,w[1]],[0,w[2]]) # col1
    plt.setp(lines, color=colors[0], linewidth=6.0)

def plot_xyz_axis(ax):
	seg0to1 = np.linspace(0, 1.0, 100)
	seg0 = seg0to1 * 0.0
	# x-axis
	x = seg0to1
	y = seg0
	z = seg0
	lines = ax.plot(x, y, z, label='x-axis (RH)')
	plt.setp(lines, color='r', linewidth=4.0)


	# y-axis green
	x = seg0
	y = seg0to1
	z = seg0
	lines = ax.plot(x, y, z, label='y-axis')
	plt.setp(lines, color='g', linewidth=4.0)

	# z-axis green
	x = seg0
	y = seg0
	z = seg0to1
	lines = ax.plot(x, y, z, label='z-axis')
	plt.setp(lines, color='b', linewidth=4.0)



mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_title("rotation matrix orientation")
#theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)

#r = z**2 + 1
#x = r * np.sin(theta)
#y = r * np.cos(theta)

plot_xyz_axis(ax)


R = np.array([  [ 0.86602540378443871,  0.49999999999999999,  0.00000000],
                [-0.49999999999999999,  0.86602540378443871,  0.00000000], 
                [ 0.00000000000000000,  0.00000000000000000,  1.00000000]])


#rotation of about -74 degrees around axis (-1/3,2/3,2/3)
R = np.array([  [ 0.36000000,  0.48000000, -0.80000000],
                [-0.80000000,  0.60000000,  0.00000000], 
                [ 0.48000000,  0.64000000,  0.60000000]])

plot_rot_mat_by_col(ax, R)

theta = 0
w = np.array([-1.0/3.0, 2.0/3.0, 2.0/3.0])
plot_angle_axis(ax, theta, w)


ax.legend()

plt.show()
