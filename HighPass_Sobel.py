# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:27:17 2019

@author: vaibhav
"""

import cv2

x = cv2.imread("face.jpg",0)
z= cv2.Sobel(x,cv2.CV_64F,1,0) #(matrixname,(size_of_matrix),standard_deviation) 
cv2.imshow("test",x)
cv2.imshow("GaussianBlur",z)
cv2.waitKey()
cv2.destroyAllWindows()