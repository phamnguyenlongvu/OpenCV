# Create a paint application with adjustable colors and brush
# radius using trackbars

import numpy as np
import sys
import time
import cv2 as cv

drawing = False
radius = 0

def nothing():
    pass


# Create a black image
img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image')

# Create trackbars for color change
cv.createTrackbar('R', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('B', 'image', 0, 255, nothing)