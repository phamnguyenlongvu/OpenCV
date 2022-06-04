import cv2 as cv
from cv2 import EVENT_MOUSEMOVE
import numpy as np

# event = [i for i in dir(cv) if 'EVENT' in i]
# print(event)

drawing = False # True if mouse is pressed
mode = True # If True, draw rectangle, Press 'M' toggle to curve
ix, iy = -1, -1

# Mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix, iy, drawing, mode

    if event == cv.EVENT_LBUTTONDBLCLK:
        drawing = True
        ix, iy = x, y

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                cv.circle(img, (x, y), 5, (0, 0, 255), -1)

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
        else:
            cv.circle(img, (x, y), 20, (0, 0, 255), -1)

# Create a black image, a windown and bind the function to windown
img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)

while True:
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv.destroyAllWindows()