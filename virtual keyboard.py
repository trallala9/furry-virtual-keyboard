
import cv2
#4.import hand tracking module
from cvzone.HandTrackingModule import HandDetector
from time import sleep
#cam settings
cap = cv2.VideoCapture(0)
#1.increase the size, set HD resolution
cap.set(3, 1280)
cap.set(4, 720)

#3.track hand, creating hand detector
detector = HandDetector(detectionCon=0.8)
keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
         ["A", "S", "D", "F", "G", "H", "J", "K", "L", "Z"],
         ["X", "C", "V", "B", "N", "M", "/", ".", ",", ";"]]
finalText = ""


def drawAll(img, buttonList):

    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cv2.rectangle(img, button.pos, (x + w, y + h), (255, 0, 255), cv2.FILLED)
    # 6. creating one button with text on it
        cv2.putText(img, button.text, (x + 20, y + 60),
                    cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 5)

    return img
#7 create class for buttons
class Button():
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.size = size
        self.text = text



#9.create myButton object to show-->
#-->myButton = Button([100, 100], "Q")

#11.create list with loop to show buttons
buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([100 * j + 50, 100 * i + 50], key))




#2.create a while loop(boilerplate for vebcam)
while True:
    success, img = cap.read()
    #5.lets create two statements, for find hands and find landmarks points
    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)
    img = drawAll(img, buttonList)

    if lmList:
        for button in buttonList:
            x, y = button.pos
            w, h = button.size

            if x < lmList[8][0] < x + w and y < lmList[8][1] < y + h:
                cv2.rectangle(img, button.pos, (x + w, y + h), (175, 0, 175), cv2.FILLED)
                cv2.putText(img, button.text, (x + 20, y + 60),
                            cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 5)
                l, _, _ = detector.findDistance(8, 12, img)
                print(l)

                #when clicked
                if l < 30:
                    cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 20, y + 60),
                                cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 5)
                    finalText += button.text
                    sleep(0.15)
    cv2.rectangle(img, (50, 350), (700, 450), (175, 0, 175), cv2.FILLED)
    cv2.putText(img, finalText, (60, 430),
                cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 5)




    #img = myButton.draw(img)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
