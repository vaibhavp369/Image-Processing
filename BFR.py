# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 21:00:15 2019

@author: vaibhav
"""


import cv2

#x = cv2.imread("img2.tif",1)  
x = cv2.imread("rgb1.jpg",1)  
r= x[0:614,0:394,-1]
b = x[:,:,0]
g = x[:,:,1]

cv2.imshow("Original Image",x)
cv2.imshow("red",r)
cv2.imshow("green",g)
cv2.imshow("blue",b)
cv2.waitKey()
cv2.destroyAllWindows()
