import cv2 as cv
import numpy as np

def ex():
    hv = np.zeros((300, 300), dtype='uint8')
    cv.rectangle(hv, (25, 25), (275, 275), 255, -1)

    ht = np.zeros((300, 300), dtype='uint8')
    cv.circle(ht, (150, 150), 150, 255, -1)

    bAnd = cv.bitwise_and(hv, ht)
    cv.imshow('And', bAnd)
    cv.waitKey(0)

    bOr = cv.bitwise_or(hv, ht)
    cv.imshow('Or', bOr)
    cv.waitKey(0)

    bNot = cv.bitwise_not(hv, ht)
    cv.imshow('Not', bNot)
    cv.waitKey(0)

    bXor = cv.bitwise_xor(hv, ht)
    cv.imshow('Xor', bXor)
    cv.waitKey(0)

    cv.waitKey(0)
    cv.destroyAllWindows()

img = cv.imread(r'C:\Users\LONG VU\Desktop\OpenCV\starry_night.jpg')
print(img.shape)
r = 600 / img.shape[1]
dim = (600, int(img.shape[0] * r))
res_img = cv.resize(img, dim)

mask = np.zeros(res_img.shape[:2], dtype='uint8')
(cX, cY) = (mask.shape[1]//2, mask.shape[0]//2)
cv.rectangle(mask, (cX-100, cY-100), (cX+100, cY+100), 255, -1)
cv.imshow('Mask', mask)

masked = cv.bitwise_and(res_img, res_img, mask=mask)
cv.imshow('Masked', masked)

cv.waitKey(0)
cv.destroyAllWindows()