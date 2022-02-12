import numpy as np
import cv2 as cv

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)


while True:
    # cv.imshow('Black', img)

    # Draw a diagonal blue line with thickness of 5 px
    cv.line(img, (0, 0), (512, 512), (255, 0, 0), 1)

    # Draw rectangle
    cv.rectangle(img, (0, 0), (100, 100), (100, 100, 100), 2)

    # Draw circle
    cv.circle(img, (50, 50), 50, (100, 100, 100), 2)

    # Draw ellipse
    cv.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)

    # Draw Polygon
    pts = np.array([[50, 200], [100, 200], [130, 250], [100, 300], [50, 300], [20, 250]])
    pts = pts.reshape((-1, 1, 2))
    cv.polylines(img, [pts], True, (0, 255, 255))

    # Adding text to Images
    font = cv.FONT_HERSHEY_COMPLEX
    cv.putText(img, 'OpenCV', (200, 100), font, 2, (50, 70, 70), 3, cv.LINE_AA)
    cv.imshow('Img', img)
    if cv.waitKey(1) == ord('q'):
        break

cv.destroyAllWindows()