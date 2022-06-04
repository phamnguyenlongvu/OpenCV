import numpy as np
import cv2 as cv

img = cv.imread(r"C:\Users\LONG VU\Desktop\OpenCV\Core Operations\cat.jpg")

# Accessing RED value
print(img.item(10, 10, 2))

# Modifying RED value
img.itemset((10, 10, 2), 255)

"""
Use img.item for accessing 
img.itemset for modifying
"""
while True:
    cv.imshow('img', img)
    if cv.waitKey(1) == ord('q'):
        break

cv.destroyAllWindows()