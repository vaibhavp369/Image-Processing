# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 15:36:15 2019

@author: vaibhav
"""

import cv2

p= cv2.VideoCapture(0)



def fun(e,x,y,flags,para):
    if e == cv2.EVENT_FLAG_LBUTTON:
        global b,g,r,h
        print x,y
        print img[y,x]
        h = int(hsv[y,x,0])
#        g = int(hsv[y,x,1])
#        r = int(hsv[y,x,2])
        
cv2.namedWindow("CAM")

cv2.setMouseCallback("CAM",fun)
h= 0
#g = 0
#b= 0


d = 10

while 1:
    
    f ,img = p.read()
#    img = cv2.imread("sample.jpg")
    if f :
#        img= cv2.GaussianBlur(img,(11,11),5)
        
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        #rimg = cv2.inRange(img,(b-d,g-d,r-d),(b+d,g+d,r+d))# multimeter
        rimg = cv2.inRange(hsv,(h-d,50,50),(h+d,200,255))# multimeter
        
                
        cv2.imshow("hsv",hsv)       
        cv2.imshow("mask",rimg)       
        cv2.imshow("CAM",img)
    if cv2.waitKey(100) & 0xff == 27:
        break

cv2.destroyAllWindows()
print f 
p.release()

