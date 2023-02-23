import cv2
import numpy as np


def nothing():  # trackbar kullanımı için
    pass


cap = cv2.VideoCapture(0)

cv2.namedWindow('Settings')

cv2.createTrackbar('Lower-Hue', 'Settings', 0, 180, nothing)
cv2.createTrackbar('Lower-Saturation', 'Settings', 0, 255, nothing)
cv2.createTrackbar('Lower-Value', 'Settings', 0, 255, nothing)
cv2.createTrackbar('Upper-Hue', 'Settings', 0, 180, nothing)
cv2.createTrackbar('Upper-Saturation', 'Settings', 0, 255, nothing)
cv2.createTrackbar('Upper-Value', 'Settings', 0, 255, nothing)

font = cv2.FONT_HERSHEY_SIMPLEX

while True:

    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_hue = cv2.getTrackbarPos('Lower-Hue', 'Settings')
    lower_saturation = cv2.getTrackbarPos('Lower-Saturation', 'Settings')
    lower_value = cv2.getTrackbarPos('Lower-Value', 'Settings')
    upper_hue = cv2.getTrackbarPos('Upper-Hue', 'Settings')
    upper_saturation = cv2.getTrackbarPos('Upper-Saturation', 'Settings')
    upper_value = cv2.getTrackbarPos('Upper-Value', 'Settings')

    lower_color = np.array([lower_hue, lower_saturation, lower_value])
    upper_color = np.array([upper_hue, upper_saturation, upper_value])

    mask = cv2.inRange(hsv, lower_color, upper_color)

    kernel = np.ones((5, 5), np.uint8)

    mask = cv2.erode(mask, kernel)

    contour, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contour:

        area = cv2.contourArea(cnt)
        epsilon = 0.01 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, epsilon, True)

        x, y = approx[0][0]

        if area > 400:
            cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)
            if len(approx) == 3:
                cv2.putText(frame, 'Triangle', (x, y), font, 1, (0, 0, 0), 3)

            elif len(approx) == 4:
                cv2.putText(frame, 'Rectangle', (x, y), font, 1, (0, 0, 0), 3)

            elif len(approx) == 5:
                cv2.putText(frame, 'Pentagon', (x, y), font, 1, (0, 0, 0), 3)

            elif len(approx) == 6:
                cv2.putText(frame, 'Hexagon', (x, y), font, 1, (0, 0, 0), 3)

            else:
                cv2.putText(frame, 'Ellipse', (x, y), font, 1, (0, 0, 0), 3)



    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)

    if cv2.waitKey(3) and 0xFF == ord(' '):
        break

cap.release()
cv2.destroyAllWindows()




