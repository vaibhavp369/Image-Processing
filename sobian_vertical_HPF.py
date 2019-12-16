# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:38:33 2019

@author: vaibhav
"""
#horizontal
import cv2

x = cv2.imread("face.jpg",0)
z= cv2.Sobel(x,cv2.CV_64F,0,1) 
cv2.imshow("test",x)
cv2.imshow("GaussianBlur",z)
cv2.waitKey()
cv2.destroyAllWindows()