import cv2 as cv
import numpy as np

def apply_sliding_sindow(img, kernel, padding=0, stride=1):
    h, w =img.shape[:2]
    img_p = np.zeros([h + 2*padding, w + 2*padding])
    img_p[padding:h+padding, padding:padding+w] = img

    kernel = np.array(kernel)
    assert len(kernel.shape) == 2 and kernel.shape[0] == kernel.shape[1] # square kernel
    assert kernel.shape[0] % 2 != 0 # kernel size is old number

    k_size = kernel.shape[0]
    k_half = int(k_size/2)

    y_pos = [v for idx, v in enumerate(list(range(k_half, h-k_half))) if idx%stride==0]
    x_pos = [v for idx, v in enumerate(list(range(k_half, w-k_half))) if idx%stride==0]

    new_img = np.zeros([len(y_pos), len(x_pos)])
    for new_y, y in enumerate(y_pos):
        for new_x, x in enumerate(x_pos):
            if k_half == 0:
                pixel_val = img_p[y, x] *kernel
            else:
                pixel_val = np.sum(img[y-k_half])

