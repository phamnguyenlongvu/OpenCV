import numpy as np
import cv2 as cv

img = cv.imread(r'C:\Users\LONG VU\Desktop\OpenCV\starry_night.jpg')
re_img = cv.resize(img, (600, 400))

b, g, r = cv.split(re_img)

cv.imshow('b', b)
cv.imshow('g', g)
cv.imshow('r', r)
cv.waitKey(0)

