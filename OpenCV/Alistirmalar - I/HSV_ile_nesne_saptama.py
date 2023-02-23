import cv2
import numpy as np

cap = cv2.VideoCapture('hsv.mp4')


def nothing():
    pass


cv2.namedWindow('Trackbar')

cv2.createTrackbar('Lower-H', 'Trackbar', 0, 179, nothing)
cv2.createTrackbar('Lower-S', 'Trackbar', 0, 255, nothing)
cv2.createTrackbar('Lower-V', 'Trackbar', 0, 255, nothing)

cv2.createTrackbar('Upper-H', 'Trackbar', 0, 179, nothing)
cv2.createTrackbar('Upper-S', 'Trackbar', 0, 255, nothing)
cv2.createTrackbar('Upper-V', 'Trackbar', 0, 255, nothing)

while True:
    ret, frame = cap.read()

    frame = cv2.resize(frame, (640, 480))

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_H = cv2.getTrackbarPos('Lower-H', 'Trackbar')
    lower_S = cv2.getTrackbarPos('Lower-S', 'Trackbar')
    lower_V = cv2.getTrackbarPos('Lower-V', 'Trackbar')

    upper_H = cv2.getTrackbarPos('Upper-H', 'Trackbar')
    upper_S = cv2.getTrackbarPos('Upper-S', 'Trackbar')
    upper_V = cv2.getTrackbarPos('Upper-V', 'Trackbar')

    lower_Blue = np.array([lower_H, lower_S, lower_V])
    upper_Blue = np.array([upper_H, upper_S, upper_V])

    mask = cv2.inRange(hsv, lower_Blue, upper_Blue)

    bitwise = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('bitwise', bitwise)

    if cv2.waitKey(20) and 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
