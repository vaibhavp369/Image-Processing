# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:41:02 2019

@author: vaibhav
"""

import cv2

x = cv2.imread("face.jpg",0)
z= cv2.Laplacian(x,cv2.CV_64F) 
cv2.imshow("test",x)
cv2.imshow("Laplacian",z)
cv2.waitKey()
cv2.destroyAllWindows()