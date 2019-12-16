# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 15:36:15 2019

@author: vaibhav
"""

import cv2

x= cv2.VideoCapture(0)


while 1:
    
    f, img = x.read()
    if f :
        cv2.imshow("CAM",img)
        z= cv2.GaussianBlur(img,(11,11),5)
        rimg = cv2.inRange(img,(36,61,0),(106,115,4))# multimeter
        #rimg = cv2.inRange(img,(147,128,0),(215,117,0))# bottle
        cv2.imshow("CAM2",rimg)
    if cv2.waitKey(100) & 0xff == 27:
        break

cv2.destroyAllWindows()
print f 
x.release()

