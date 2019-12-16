# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 12:15:32 2019

@author: vaibhav
"""

import cv2

x = cv2.imread("png.png",0)
cv2.imshow("img",x)
y= cv2.waitKey()
if (y== 115):
  cv2.imwrite("test7.jpg",x)
  cv2.destroyAllWindows()
else:
    cv2.destroyAllWindows()