import numpy as np
import cv2 as cv

# Load two images
img2 = cv.imread(r"C:\Users\LONG VU\Desktop\OpenCV\Core Operations\Bk.jpg")
img1 = cv.imread(r"C:\Users\LONG VU\Desktop\OpenCV\Core Operations\cat.jpg")

# Create a ROI in img1
rows, cols, channels = img2.shape
ROI = img1[0:rows, 0: cols]

# Create a mask of logo and create its inverse mark also
img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)

# Black out the area of logo in ROI
img_bg = cv.bitwise_and(ROI, ROI, mask=mask_inv)

# Take only region of logo from lodo image
img_fg = cv.bitwise_and(img2, img2, mask=mask)

# Put logo in ROI and modify the main image
dst = cv.add(img_bg, img_fg)
img1[0:rows, 0:cols] = dst

cv.imshow('img', mask)
cv.waitKey(0)
cv.destroyAllWindows()