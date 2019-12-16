import numpy as np
import cv2

image = cv2.imread("mulcircle.png",1)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)



circles = cv2.HoughCircles(gray, cv2.cv.CV_HOUGH_GRADIENT, 1.2, 100,param1=1,param2=20)
 
# ensure at least some circles were found
if circles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	#circles = np.round(circles[0, :]).astype("int")
 
	# loop over the (x, y) coordinates and radius of the circles
	for x,y,r in circles[0]:
            cv2.circle(image,(x,y),r,(255,0,0),4)

cv2.imshow("output", image)
cv2.waitKey(0)
cv2.destroyAllWindows()