'''
Threshing là phương pháp khi chúng ta muốn chuyển đổi từ ảnh xám thành
ảnh nhị phân. Phương pháp là xét một ngưỡng p, cài đặt toàn bộ điểm ảnh 
có giá trị nhỏ hơn p thành giá trị 0, những điểm ảnh còn lại có giá trị 1.
Như vậy ảnh màu -> ảnh xám -> ảnh nhị phân.
Áp dụng xét ngưỡng trong xử lí ảnh nhằm tập trung vào các đối tượng hoặc
vùng quan tâm.
'''

"""
Phương pháp xét Threshing cơ bản: Định nghĩa một ngưỡng cứng T, giá trị nhỏ hơn
T được gán giá trị mới là 0, còn giá trị lớn hơn T được gán giá trị mới là 255.
"""

import cv2 as cv
from cv2 import blur
import numpy as np

img = cv.imread(r'C:\Users\LONG VU\Desktop\OpenCV\starry_night.jpg')
rs_img = cv.resize(img, (400, 300))
rs_img = cv.cvtColor(rs_img, cv.COLOR_RGB2GRAY)
blurred = cv.GaussianBlur(rs_img, (15, 15), 0) # Kỹ thuật làm mờ Gaussian giúp làm mờ viền, loại bỏ đường nét
# cv.imshow('Anh demo', rs_img) 

(T, thresh) = cv.threshold(blurred, 155, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh binary', thresh)

(T, thresh_inverse) = cv.threshold(blurred, 155, 255, cv.THRESH_BINARY_INV) 
# cv.imshow('Thresh binary inverse', thresh_inverse)

# cv.imshow('Masked', cv.bitwise_and(rs_img, rs_img, mask=thresh_inverse))

"""
Phương pháp thứ 2 là chọn ngưỡng thích ứng. Nhược điểm cơ bản của phương pháp trên là phải chọn thủ công cố định 
ngưỡng cứng. Để lựa chọn được giá trị tối ưu này cần phải trải qua nhiều lần kiểm nghiệm. 
"""
thresh_adaptive = cv.adaptiveThreshold(blurred, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 4)
cv.imshow('Thresh adaptive', thresh_adaptive)
"""
Phương pháp này tìm giá trị ngưỡng tối ưu trên 1 blocksize điểm ảnh, ở đây là 11 x 11. Phương pháp tính ngưỡng là
ADAPTIVE_THRESH_GAUSSIAN_C, Tham số C= 4 cuối cùng là giá trị trừ đi giá trị trung bình để điều chỉnh ngưỡng.
"""

"""
Ngoài ra còn có phương pháp Otsu và Riddler-Calvard. Phương pháp này giả sử tồn tại 2 đỉnh của biểu đồ histogram. Giá 
trị ngưỡng tối ưu sẽ tìm giữa 2 đỉnh này.
"""

cv.waitKey(0)
cv.destroyAllWindows()



