from configparser import Interpolation
from turtle import color
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def hist_gray():
    img = cv.imread(r'C:\Users\LONG VU\Desktop\OpenCV\starry_night.jpg')
    cvtimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    rs_img = cv.resize(cvtimg, (500, 300))
    cv.imshow('Demo', rs_img)

    hist = cv.calcHist([rs_img], [0], None, [256], [0, 256])

    plt.figure()
    plt.title("Bieu do anh xam")
    plt.xlabel('Nhom')
    plt.ylabel('# of Pixel')

    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()

    cv.waitKey(0)
    cv.destroyAllWindows()

img = cv.imread(r'C:\Users\LONG VU\Desktop\OpenCV\starry_night.jpg')
rs_img = cv.resize(img, (500, 300))
# cv.imshow('Demo', rs_img)

chans = cv.split(rs_img)
colors = ("b", "g", "r")
# plt.figure()
# plt.title('Bieu do mau sac')
# plt.xlabel('Nhom')
# plt.ylabel('# of pixels')

# for (chan, color) in zip(chans, colors):
#     hist = cv.calcHist([chan], [0], None, [256], [0, 256])
#     plt.plot(hist, color=color)
#     plt.xlim([0, 256])

# plt.show()

### 2D histogram for 2 color
# fig = plt.figure()

# ax = fig.add_subplot(131)
# hist = cv.calcHist([chans[1], chans[0]], [0, 1], None, [32, 32], [0, 256, 0, 256])
# p = ax.imshow(hist, interpolation = "nearest")
# ax.set_title("2D color histogram for G and B")
# plt.colorbar(p)

# ax = fig.add_subplot(132)
# hist = cv.calcHist([chans[1], chans[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
# p = ax.imshow(hist, interpolation = "nearest")
# ax.set_title("2D color histogram for G and R")
# plt.colorbar(p)

# ax = fig.add_subplot(133)
# hist = cv.calcHist([chans[2], chans[0]], [0, 1], None, [32, 32], [0, 256, 0, 256])
# p = ax.imshow(hist, interpolation = "nearest")
# ax.set_title("2D color histogram for r and B")
# plt.colorbar(p)


### 3D histogram for 3 color
gray = cv.cvtColor(rs_img, cv.COLOR_BGR2GRAY)

fig = plt.figure()
ax = fig.add_subplot(121)
hist = cv.calcHist([gray], [0], None, [256], [0, 256])
ax.plot(hist)

eq = cv.equalizeHist(gray)
ax = fig.add_subplot(122)
hist = cv.calcHist([eq], [0], None, [256], [0, 256])
ax.plot(hist)

cv.imshow('HE', np.hstack([gray, eq]))



plt.show()
cv.waitKey(0)
cv.destroyAllWindows()