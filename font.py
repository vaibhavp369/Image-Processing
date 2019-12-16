# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 12:45:59 2019

@author: vaibhav
"""

import cv2

x = cv2.imread("rgb1.jpg",1)
b,g,r = cv2.split(x)

#f= cv2.FONT_HERSHEY_COMPLEX
#cv2.putText(x,"RGB",(100,100),f,4,(255,90,0),2)
cv2.imshow("blue",b)
cv2.imshow("green",g)
cv2.imshow("red",r)
c=cv2.merge((b,g,r))
cv2.imshow("merge",c)
cv2.waitKey()
cv2.destroyAllWindows()