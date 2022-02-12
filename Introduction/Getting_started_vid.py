from cv2 import flip
import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)
if not cap.isOpened(): # Check whether cap is initialized or not.
    print("Cannot open camera")
    exit()
print(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv.CAP_PROP_FRAME_WIDTH))
# ret = cap.set(cv.CAP_PROP_FRAME_HEIGHT, 240)
# ret = cap.set(cv.CAP_PROP_FRAME_HEIGHT, 320)

# Save a video capture
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('out.avi', fourcc, 20.0, (640, 480))

while True:
    # Capture frame by frame
    ret, frame = cap.read()

    # if frame is read correctly, ret is True
    if not ret:
        print("Cann't recieve frame (stream end?). Exiting ...")
        break

    # frame = cv.flip(frame, 0)

    # write the flipped frame
    out.write(frame)

    # Our operations on the frame com here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Displae the resulting frame
    cv.imshow('frame', gray)
    # cv.imshow('frame', frame) -> This instance for RBG
    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
out.release()
cv.destroyAllWindows()