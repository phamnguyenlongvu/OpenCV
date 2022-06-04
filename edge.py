"""
Trong mỗi bức ảnh, những điểm ảnh có độ sáng chênh lệch nhiều với những điểm ảnh lân cận được gọi là điểm cạnh.
Tập hợp của các điểm cạnh tạo nên cấu trúc vật thể.

Gradient của ảnh: Trong xử lí ảnh, gradient chính là độ dốc của mức sáng - sự thay đổi các giá trị trong điểm ảnh.
Vùng ảnh trơn - các giá trị ảnh lân cận có giá trị gần bằng nhau, khi đó đạo hàm sẽ có kết quả gần bằng 0. Đạo hàm 
bằng 0 thể hiện không có sự biến đổi về mức sáng. Điều này có nghĩa độ dốc trên vùng ảnh trơn gần như bằng 0. Đạo 
hàm dương thể hiện biến thiên của ảnh sáng đang có chiều hướng đi lên, ngược lại, đạo hàm âm tại một điểm ảnh thể
hiện biến thiên của mức sáng đang giảm dần.
"""

import cv2 as cv
from cv2 import blur
import numpy as np

img = cv.imread(r'C:\Users\LONG VU\Desktop\OpenCV\starry_night.jpg')
rs_img = cv.resize(img, (400, 300))
rs_img = cv.cvtColor(rs_img, cv.COLOR_RGB2GRAY)

lap = cv.Laplacian(rs_img, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

cv.waitKey(0)
cv.destroyAllWindows()