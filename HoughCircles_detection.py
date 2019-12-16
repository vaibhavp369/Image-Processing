# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 16:03:02 2019

@author: vaibhav
"""

import cv2
import numpy as np

cimg = cv2.imread("mulcircle.png",1)
#rimg = cimg[:,:,1]
rimg = cv2.inRange(cimg,(0,255,0),(0,255,0))
#img = cv2.cvtColor(cimg,cv2.COLOR_BGR2GRAY)
#
#img = cv2.medianBlur(img,5)
#circles = cv2.HoughCircles(img,cv2.cv.CV_HOUGH_GRADIENT,1,20,param1=50,param2=30)
#print circles
#for i in circles[0]:
#    print "center", i[0],i[1],"radius: ",i[2]
#    cv2.circle(cimg,(i[0],i[1]),i[2],(0,0,255),5)

cv2.imshow("detected_ciecle",rimg)
cv2.imshow("cir",cimg)
cv2.waitKey()
cv2.destroyAllWindows()
