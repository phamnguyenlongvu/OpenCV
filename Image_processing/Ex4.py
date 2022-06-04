# Smoothing Images
'''
Low pass filters(LPF) -> helps in removing noise
High pass filters(HPF) -> help in finding edges in images
'''

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def convolution(): # image fitering
    img = cv.imread(r"C:\Users\LONG VU\Desktop\OpenCV\Core Operations\cat.jpg")
    kernel = np.ones((5,5), np.float32) / 25
    dst = cv.filter2D(img, -1, kernel=kernel)
    # cv.imshow('img', img)
    plt.subplot(121)
    plt.imshow(img)
    plt.title("Original")
    plt.xticks([])
    plt.yticks([])
    plt.subplot(122)
    plt.imshow(dst)
    plt.title("Averaging")
    plt.xticks([])
    plt.yticks([])
    plt.show()


def image_blurring():
    
# convolution()