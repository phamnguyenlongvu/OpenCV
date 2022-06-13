import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
 
class Button:
    def __init__(self, pos, width, heigh, value):
        self.pos = pos
        self.width = width
        self.heigh = heigh
        self.value = value

    def draw(self, img):
        cv.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.heigh), (255, 255, 255), cv.FILLED)
        cv.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.heigh), (0, 0, 0), 3)
        cv.putText(img, self.value, (self.pos[0] + 20, self.pos[1] + 60), cv.FONT_HERSHEY_COMPLEX, 2, (50, 50, 50), 2)

    def checkClick(self, x, y):
        if self.pos[0] < x < self.pos[0] + self.width and self.pos[1] < y < self.pos[1] + self.heigh:
            cv.rectangle(img, (self.pos[0] + 3, self.pos[1] + 3), (self.pos[0] + self.width - 3, self.pos[1] + self.heigh -3), (255, 255, 255), cv.FILLED)
            cv.putText(img, self.value, (self.pos[0] + 25, self.pos[1] + 80), cv.FONT_HERSHEY_COMPLEX, 5, (0, 0, 0), 5)
            return True
        else:
            return False

# Use webcam
cap = cv.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Create Buttons
value = [['7', '8', '9', '*'],
         ['4', '5', '6', '/'],
         ['1', '2', '3', '+'],
         ['0', '.', '=', '-']]

buttonList = []
for y in range(4):
    for x in range(4):
        xpos = x*100 + 800
        ypos = 150 + y*100
        buttonList.append(Button((xpos, ypos), 100, 100, value[y][x]))

myEquation = ''
delayCounter = 0

# Loop
while True:
    # Get image from webcam
    success, img = cap.read()
    img = cv.flip(img, 1)

    hands= detector.findHands(img, flipType=False)

    cv.rectangle(img, (800, 70), (1200, 170), (255, 255, 255), cv.FILLED)
    cv.rectangle(img, (800, 70), (1200, 170), (0, 0, 0), 3)
    #Draw button
    for button in buttonList:
        button.draw(img)

    # Check for hand
    if hands:
        # Fine distance between finger:
        hand = hands[0]
        if hand:
            lmList = hand[0]['lmList']
            # print(lmList[8], lmList[12])
            point1 = (lmList[8][0], lmList[8][1])
            point2 = (lmList[12][0], lmList[12][1])
            length, _, img= detector.findDistance(point1, point2, img)
            # print(length)
            x, y = point1

            if length < 50 and delayCounter == 0:
                for i, button in enumerate(buttonList):
                    if button.checkClick(x, y):
                        myValue = value[int(i/4)][int(i%4)]
                        print(myValue)
                        if myValue == '=':
                            myEquation = str(eval(myEquation))
                        else: myEquation += myValue
                        delayCounter = 1

    if delayCounter != 0: 
        delayCounter += 1
        if delayCounter > 10:
            delayCounter = 0

    # Display the Equatation
    cv.putText(img, myEquation, (810, 130), cv.FONT_HERSHEY_PLAIN, 2, (50, 50, 50), 2)

    key = cv.waitKey(1)
    cv.imshow('Frame', img)
    if key == ord('c'):
        myEquation = ''