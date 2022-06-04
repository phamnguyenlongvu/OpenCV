import numpy as np
import cv2 as cv

def nothing(x):
    pass

# Create a black image, a windown
img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow('image')

# Create trackbars for color change
cv.createTrackbar('R', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('B', 'image', 0, 255, nothing)

# Create switch for ON/OFF functionality
switch = '0: OFF \n 1: ON'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while True:
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    r = cv.getTrackbarPos('R', 'image')
    g = cv.getTrackbarPos('G', 'image')
    b = cv.getTrackbarPos('B', 'image')
    S = cv.getTrackbarPos(switch, 'image')

    if S == 0:
        img[:] = 0
    else:
        img[:] = [r,g,b]

cv.destroyAllWindows()
    
