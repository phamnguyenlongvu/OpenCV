import numpy as np
import cv2 as cv
import random

def func1():
	frame = np.ones((300, 300, 3), dtype='uint8')

	blue = (0, 255, 0)
	cv.line(frame, (0, 0), (300, 300), blue, 1)

	red = (0, 0, 255)
	cv.line(frame, (0, 300), (300, 0), red, 2)

	white = (255, 255, 255)
	cv.rectangle(frame, (75, 75), (225, 225), white, -1)

	black = (0, 0, 0)
	for i in range(0, 90, 15):
		cv.circle(frame, (150, 150), i, black, 1)

	cv.imshow('Frame', frame)
	cv.waitKey(0)
	cv.destroyAllWindows()

frame = np.ones((400, 400, 3), dtype='uint8')
for i in range(0, 10):
	r = np.random.randint(0, 200)
	c = np.random.randint(0, 256, 3).tolist()
	pt = np.random.randint(0, 400, 2)
	cv.circle(frame, pt, r, c, -1)

cv.imshow('Frame', frame)
cv.waitKey(0)
cv.destroyAllWindows()