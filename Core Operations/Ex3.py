# Performamce measurement and improvement techniques
import cv2 as cv
import numpy as np
import time

img1 = cv.imread(r"C:\Users\LONG VU\Desktop\OpenCV\Core Operations\cat.jpg")

# e1 = cv.getTickCount()
t1 = time.time()
for i in range(5, 49, 2):
    img1 = cv.medianBlur(img1, i)
# e2 = cv.getTickCount()
# t = (e2 - e1)/cv.getTickFrequency()
t2 = time.time()
t = t2 - t1
print(t)

# There are several techniques and coding method to exploit
# maximum performance
# Avoid using loops in Python as much as posible
# Vectorize the algorithm/code to the maximum extent possible
# Exploit the cache coherence
# Never make copies of an array unless it is necessary