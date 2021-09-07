
import cv2
#4.import hand tracking module
from cvzone.HandTrackingModule import HandDetector
#cam settings
cap = cv2.VideoCapture(0)
#1.increase the size, set HD resolution
cap.set(3, 1280)
cap.set(4, 720)

#3.track hand, creating hand detector
detector = HandDetector(detectionCon=0.8)
#7 create class for buttons
class Button():
    def __init__(self,pos,text,size=[100,100]):
        self.pos = pos
        self.size = size
        self.text = text



#2.create a while loop(boilerplate for vebcam)
while True:
    success, img = cap.read()
    #5.lets create two statements, for find hands and find landmarks points
    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)


    cv2.rectangle(img,(100, 100), (200, 200), (255, 0, 255),cv2.FILLED)
    #6. creating one button with text on it
    cv2.putText(img, "A", (118,170), cv2.FONT_HERSHEY_PLAIN,5,(255,255,255), 5)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
