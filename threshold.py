# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 13:41:50 2019
# -*- coding: utf-8 -*-
"""








import cv2

x = cv2.imread("grade.jpg",0) 
y,c1 = cv2.threshold(x,200,250,cv2.THRESH_BINARY) 
y,c2 = cv2.threshold(x,125,250,cv2.THRESH_BINARY_INV) 
y,c3 = cv2.threshold(x,125,250,cv2.THRESH_TOZERO) 
y,c4 = cv2.threshold(x,125,250,cv2.THRESH_TOZERO_INV) 
y,c5 = cv2.threshold(x,125,250,cv2.THRESH_TRUNC) 
cv2.imshow("binary",c1)
cv2.imshow("binary_inv",c2)
cv2.imshow("tozero",c3)
cv2.imshow("tozero inv",c4)
cv2.imshow("trunk",c5)

cv2.imshow("original img",x)
cv2.waitKey()
cv2.destroyAllWindows()


