# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 14:14:31 2019

@author: vaibhav
"""
import cv2

x = cv2.imread("face.jpg",0)
y=cv2.blur(x,(3,3))  
cv2.imshow("test",x)
cv2.imshow("blur img",y)
cv2.waitKey()
cv2.destroyAllWindows()
