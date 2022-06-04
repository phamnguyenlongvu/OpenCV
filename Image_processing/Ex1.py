# Changing Colorspaces
import cv2 as cv
from cv2 import COLOR_BGR2HSV
import numpy as np

# flags = [i for i in dir(cv) if i.startswith('COLOR_')]
# print(flags)

"""
Object Tracking
- Tack each frame of the video
- Convert from BGR -> HSV color space
- We threshold the HSV image for a range of blue color
- Now extract the blue object alone, we can do whatever we want on that image
"""

cap = cv.VideoCapture(0)
while True:
    # take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # Threshold the HSV image to get only blue colors
    blue_mask = cv.inRange(hsv, lower_blue, upper_blue)

    # range of green color
    lower_green = np.array([50, 50, 120])
    upper_green = np.array([70, 255, 255]) 
    green_mask = cv.inRange(hsv, lower_green, upper_green)

    # Bitwise-AND mask and original image
    mask = green_mask + blue_mask # A way to extract more than one colored object simultaneously, we just add them togeters
    res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow('res', res)

    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()
    
'''
There is a simplest way to find HSV values from BGR values
green = np.uint8([[[0,255,0]]])
hsv_green = cv.cvtColor(green, cv.COLOR_BGR2HSV)
now we take [h-10, 100, 100] and [h+10, 255, 255]
'''