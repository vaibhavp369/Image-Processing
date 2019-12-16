# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 19:52:38 2019

@author: vaibhav
"""

import cv2
x = cv2.imread("rgb1.jpg",1)
b,g,r = cv2.split(x)
cv2.imshow("original img",x)
cv2.imshow("red",r)
cv2.imshow("blue",b)
cv2.imshow("green",g)
cv2.waitKey(10000)
cv2.destroyAllWindows()