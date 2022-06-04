'''
Hiện tượng ảnh mờ, ảnh nhòe là hiện tượng các điểm ảnh trong 
bức ảnh bị trộn lẫn với các giá trị ảnh xung quanh tạo thành 
một hỗn hợp các điểm ảnh có giá trị gần nhau.

Kỹ thuật này có thể dùng trong tác vụ xử lý ảnh như xóa mụn
mịn da. Đồng thời cũng hộ trợ trong quá trình phát hiện cạnh
hoặc đánh giá ngưỡng giá trị.
'''
import cv2 as cv
import numpy as np
img = cv.imread(r'C:\Users\LONG VU\Desktop\OpenCV\starry_night.jpg')

rs_img = cv.resize(img, (400, 300))
cv.imshow('Oringal img', rs_img)

'''
Kỹ thuật tính trung bình. Sử dụng một kernel (KxK) trượt dọc từ trái 
sang phải và từ trên xuống dưới. 
'''
blurred = np.hstack([
    cv.blur(rs_img, (3, 3)), 
    cv.blur(rs_img, (5, 5)),
    cv.blur(rs_img, (7, 7))
])

cv.imshow('Averaged', blurred) # Kernel với K càng lớn thì ảnh càng mờ

'''
Kỹ thuật Gausian tương tự như kỹ thuật thứ nhất, nhưng thay vì tính trung
bình đơn giản thì sử dụng phương pháp tính trung bình có đánh trọng số, 
trong đó, điểm ảnh gần tâm thì có trọng số lớn hơn phần còn lại. Kết quả ảnh
bị mờ ít hơn và tự nhiên hơn.
'''

blurred_gau = np.hstack([
    cv.GaussianBlur(rs_img, (3, 3), 0),
    cv.GaussianBlur(rs_img, (5, 5), 0),
    cv.GaussianBlur(rs_img, (7, 7), 0)
])

cv.imshow('Gaussian', blurred_gau)

'''
Kỹ thuật trung vị hiệu quả trọng việc ảnh chụp bị sạn. Vì mỗi điểm ảnh trung 
tâm luôn được thay bằng cường độ điểm ảnh tồn tại trong ảnh, tồn tại trong kernel
nên tạo ra phân bố đều các điểm ảnh khiến ảnh trở lên mịn hơn. 
'''

blurred_median = np.hstack([
    cv.medianBlur(rs_img, 3),
    cv.medianBlur(rs_img, 5),
    cv.medianBlur(rs_img,  7)
])
cv.imshow('Median', blurred_median)

'''
Kỹ thuật làm mờ song phương là quá trình giảm nhiễu cho ảnh, tuy nhiên quá trình này 
có thể gây ra hiện tượng mất góc cạnh trên ảnh. Phương pháp này áp dụng 2 hàm Gauss.
Hàm Gauss thứ nhất chỉ bao gồm các điểm ảnh xuất hiện gần nhau theo tọa độ (x, y) trong
ảnh. Hàm Gauss thứ hai mô hình hóa phân bố điểm ảnh lân cận, đảm bảo chỉ có những điểm ảnh
tương tự mới được tính toán làm mờ. Phương pháp này ứng dụng trong các ứng dụng làm đẹp che
khuyết điểm. 
'''

blurred_bilateral = np.hstack([
    cv.bilateralFilter(rs_img, 5, 21, 21),
    cv.bilateralFilter(rs_img, 7, 31, 31),
    cv.bilateralFilter(rs_img, 9, 41, 41)
])
cv.imshow('Bilateral', blurred_bilateral) # Tuy nhiên phương pháp này chậm hơn đánh kể.

cv.waitKey(0)
cv.destroyAllWindows()