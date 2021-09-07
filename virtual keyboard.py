
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
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.size = size
        self.text = text
        x,y = self.pos
        w,h = self.size
        cv2.rectangle(img, self.pos, (x+w, y+h), (255, 0, 255), cv2.FILLED)
        # 6. creating one button with text on it
        cv2.putText(img, self.text, (x+20, y+60),
                    cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 5)

        

#9.create myButton object to show-->
#-->myButton = Button([100, 100], "Q")

#11.create list with loop to show buttons
buttonList = []

for x in range (0,5):
    buttonList.append(Button([100*x+50, 100], "Q"))




#2.create a while loop(boilerplate for vebcam)
while True:
    success, img = cap.read()
    #5.lets create two statements, for find hands and find landmarks points
    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)

    img = myButton.draw(img)


    cv2.imshow("Image", img)
    cv2.waitKey(1)
