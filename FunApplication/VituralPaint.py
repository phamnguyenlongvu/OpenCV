import cv2 as cv
from cvzone.HandTrackingModule import HandDetector

class blockColor:
    def __init__(self, pos, width, value):
        self.pos = pos
        self.width = width
        self.value = value

    def draw(self, img):
        cv.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.width), self.value, cv.FILLED)

    def check(self, x, y):
        if self.pos[0] < x < self.pos[0] + self.width and self.pos[1] < y < self.pos[1] + self.width:
            return True
        return False
        
cap = cv.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector  = HandDetector(detectionCon=0.8, maxHands=1)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

colorRecommend = [black, red, green, blue, white]
colorList = []
for i in range(5):
    xpos = 1180
    ypos = i*100
    colorList.append(blockColor((xpos, ypos), 100, colorRecommend[i]))

value = (255, 255, 255)   
while True:
    _, img = cap.read()
    img = cv.flip(img, 1)
    hands = detector.findHands(img, flipType=False)
    for color in colorList:
        color.draw(img)
    blockMix = blockColor((1080, 520), 200, value)    
    blockMix.draw(img)
    if hands:
        hand = hands[0]
        if hand:
            lmList = hand[0]["lmList"]
            point1 = (lmList[4][0], lmList[4][1])
            point2 = (lmList[8][0], lmList[8][1])
            length, _, img = detector.findDistance(point1, point2, img)
            # print(length)
            x, y = ((lmList[4][0] + lmList[8][0])/2, (lmList[4][1]+lmList[8][1])/2)

            for (i, color) in enumerate(colorList):
                if color.check(x, y):
                    value = (int((colorRecommend[i][0] + value[0])/2), int((colorRecommend[i][1] + value[1])/2), int((colorRecommend[i][2] + value[2])/2))

    cv.imshow('Frame', img)
    cv.waitKey(1)
