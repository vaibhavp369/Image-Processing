# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:45:46 2019

@author: vaibhav
"""

import cv2

x = cv2.imread("img1.tif",0)
#y=cv2.blur(x,(3,3)) #to more fine edge use blur
z= cv2.Canny(x,100,200) 
cv2.imshow("test",x)
cv2.imshow("canny",z)
cv2.waitKey()
cv2.destroyAllWindows()