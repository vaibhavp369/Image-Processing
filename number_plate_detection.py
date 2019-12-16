




import cv2  
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_russian_plate_number.xml') 
cap = cv2.VideoCapture(0) 
while 1: 
    img = cv2.imread("plate.jpg")
#    ret, img = cap.read()  
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
    for (x,y,w,h) in faces: 
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)  
         # Detects eyes of different sizes in the input image 
    cv2.imshow('img',img) 
    k = cv2.waitKey(30) & 0xff
    if k == 27: 
        break
cap.release() 
cv2.destroyAllWindows() 