# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 15:36:15 2019

@author: vaibhav
"""

import cv2

x= cv2.VideoCapture(0)
while 1:
    
    f, img = x.read()
    if f :
        cv2.imshow("CAM",img)

    if cv2.waitKey(100) & 0xff == 27:
        break

cv2.destroyAllWindows()
print (f)
x.release()

