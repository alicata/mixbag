#! /usr/bin/python
"""

TrajLogger, trajectory and image stream logger

traj data:
timestamp in millis, [x, y], [w,h]


"""
import sys
import os
import time
import cv2
import numpy as np

class TrajLogger:
    def __init__(self, filename):
        self.traj = []
        self.maxCols = 8  # num image columns in image matrix
        self.spf = 500    # time in millis between image samples
        self.frameMap = {}
        self.frameTs = []
        self.init(filename)

    def init(self, filename):
        self.filename = filename

    def add(self, millis, pos, size):
        self.traj.append((millis, pos, size))

    def getFrameName(self, millis):
        fps10 = millis/self.spf
        frameName  = "%04d" % int(fps10)
        return frameName

    def addImage(self, millis, frame):
        frameName  = self.getFrameName(millis)

        if frameName in self.frameMap:
            return

        frame = cv2.resize(frame, (320,240))
        filename = "trajLogger_img%04d.jpg" % int(millis/self.spf)
        cv2.imwrite(filename,frame)
        
        self.frameMap[frameName] = frame

        # add unique timestamps only
        if len(self.frameTs) == 0:
            self.frameTs.append(millis)

        lastTs = self.frameTs[len(self.frameTs)-1]

        if lastTs < millis:
            self.frameTs.append(millis)
        
    def saveTrackLog(self):
        print 'saving tracking file %s' % self.filename
        f = open(self.filename, 'w')

        for item in self.traj:
            millis = item[0]
            pos = item[1]
            size = item[2]
            line = "%.2f %d %d %d %d\n" % (millis, pos[0], pos[1], size[0], size[1])
            f.write(line)
        f.close()

    def addToRow(self, imgLong, frame):
        if len(imgLong) == 0:
            imgLong = frame
        else: 
            imgLong = np.concatenate((imgLong, frame), axis=1)

        return imgLong

    def addToMatrix(self, imgMat, imgLong):
        if len(imgMat) == 0:
            imgMat = imgLong
        else:
            imgMat = np.concatenate((imgMat, imgLong), axis=0)
        return imgMat

    """
    saveImageList: save a list of images as a image matrix
    """
    def saveImageList(self):
        imgLong = []
        imgMat = []

        
        itemNum = 0
        rowNo = 0

        for millis in self.frameTs:
            frameName  = self.getFrameName(millis)
            print "%f frame %s" % (millis, frameName)
            frame = self.frameMap[frameName]

            imgLong = self.addToRow(imgLong, frame)

            if ((itemNum+1) % self.maxCols == 0):
                filerow = 'traj%d.jpg' % rowNo
                print "save trajectory row %d %s" % (rowNo, filerow)
                cv2.imwrite(filerow, imgLong)

                imgMat = self.addToMatrix(imgMat, imgLong)

                # reset to next row
                rowNo = rowNo + 1
                imgLong = []
            
            itemNum = itemNum + 1
        
        if imgMat is None or len(imgMat) < 1:
            print "[TrajLogger] cannot save empty image matrix"
        else:
                cv2.imwrite('trajLogger.jpg', imgMat)

    def save(self):
        self.saveTrackLog()
        self.saveImageList()

if __name__ == "__main__":

    print ("start trajLogger test: 10 black images and 10 trajectory timestamps each second (1000 millis)")

    logger = TrajLogger("test.traj.txt")
    
    """
    create a 3 rows x 8 columns matrix of random images in memory

    """
    for k in range(8*3): 
        t = k*1000
        print " %d millisec: " % t
        logger.add(float(t), (0,0), (20,20))
        logger.addImage(t, np.random.rand(30,20)*255)  # np.zeros((100, 100)))

    logger.save()