# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 20:43:57 2019

@author: vaibhav
"""






import cv2

x = cv2.imread("rgb1.jpg",1)  
cv2.imshow("test",x)
cv2.waitKey()
cv2.destroyAllWindows()