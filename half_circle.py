# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 15:07:26 2019

@author: vaibhav
"""


# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 13:24:00 2019

@author: vaibhav
"""
import cv2

x = cv2.imread("mulcircle.png",0)
r,y=cv2.threshold(x,100,255,cv2.THRESH_BINARY_INV)
c,a= cv2.findContours(y,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


#cv2.rectangle(x,tuple(c[0][0][0]),tuple(c[0][2][0]),(160,56,80),5)
cv2.drawContours(x,c,-1,(160,56,80),5)

#cv2.imshow("rect",u)
cv2.imshow("original",x)
#cv2.imshow("thres",y)

cv2.waitKey()
cv2.destroyAllWindows()
