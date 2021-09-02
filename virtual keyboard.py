import cv2

cap = cv2.VideoCapture(0)
#increase the size, set HD resolution
cap.set(3, 1280)
cap.set(4, 720)
#create a while loop(boilerplate for vebcam)
while True:
    success, img = cap.read()
    cv2.imshow("Image", img)
    cv2.waitKey(1)