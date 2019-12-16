# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 13:07:04 2019

@author: vaibhav
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 12:45:59 2019

@author: vaibhav
"""

import cv2

y = cv2.imread("rgb1.jpg",0)
x= cv2.imread("download.jpg",0)
c = x[70:170,0:100]
d = y[255:355,200:300]
cv2.imshow("test",c)
cv2.imshow("test2",d)
w=cv2.addWeighted(c,0.1,d,0.9,0)
cv2.imshow("test3",w)

#a,b,c = x.shape
#print "y:",a
#print "x:",b
#print "z:",c
#cv2.line(x,(0,0),(b/2,a/2),(255,0,0),4)
#cv2.imshow("img1",x)
#cv2.imshow("img2",y)

cv2.waitKey()
cv2.destroyAllWindows()