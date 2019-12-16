# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 16:03:02 2019

@author: vaibhav
"""

import cv2
import numpy as np

cimg = cv2.imread("obj3.jpg",1)
#rimg = cv2.inRange(cimg,(0,255,0),(0,255,0))

def fun(e,x,y,flags,para):
    if e == cv2.EVENT_FLAG_LBUTTON:
        print x,y
        print cimg[y,x]

cv2.namedWindow("cir")
cv2.setMouseCallback("cir",fun)
#cv2.imshow("detected_ciecle",rimg)
cv2.imshow("cir",cimg)
cv2.waitKey()
cv2.destroyAllWindows()
