# Geometric Tranformations of Images
import numpy as np
import cv2 as cv

img = cv.imread(r"C:\Users\LONG VU\Desktop\OpenCV\Core Operations\cat.jpg")

# Scaling 
res = cv.resize(img, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)

# Translation
rows, cols, _ = img.shape

M = np.float32([[1, 0, 100], [0, 1, 100]])
res1 = cv.warpAffine(img, M, (cols, rows))

# Rotation
N = cv.getRotationMatrix2D(((cols - 1)/2.0, (rows - 1)/2.0), 90, 1)
dst = cv.warpAffine(img, N, (cols, rows))

# Affine transformation
# Perspective Transformation
cv.imshow('res', dst)
cv.waitKey(0)

cv.destroyAllWindows()