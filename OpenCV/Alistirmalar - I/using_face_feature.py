import cv2
import numpy as np
import math


def findMaxContour(contour):

    max_index = 0
    max_area = 0

    for i in range(len(contour)):
        area_face = cv2.contourArea(contour[i])

        if max_area < area_face:
            max_area = area_face
            max_index = i

        try:
            c = contour[max_index]

        except:
            contour = [0]
            c = contour[0]

        return c


cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    roi = frame[75:425, 125:475]  # frame[y1:y2, x1:x2]

    cv2.rectangle(frame, (125, 75), (475, 425), (0, 0, 255), 0)

    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    lower_color = np.array([0, 45, 79], dtype=np.uint8)
    upper_color = np.array([17, 255, 255], dtype=np.uint8)

    mask = cv2.inRange(hsv, lower_color, upper_color)
    kernel = np.ones((3, 3), dtype=np.uint8)

    mask = cv2.dilate(mask, kernel, iterations=1)
    mask = cv2.medianBlur(mask, 15)

    contour, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contour) > 0:

        c = findMaxContour(contour)

        extLeft = tuple(c[c[:, :, 0].argmin()][0])  # görevi en küçük x leri bulmaktır
        extRight = tuple(c[c[:, :, 0].argmax()][0])
        extTop = tuple(c[c[:, :, 1].argmin()][0])  # 0 x demek 1 y demek ondan buraya 1 yazıldı
        extBot = tuple(c[c[:, :, 1].argmax()][0])

        cv2.circle(roi, extLeft, 5, (0, 255, 0), 2)
        cv2.circle(roi, extRight, 5, (0, 255, 0), 2)
        cv2.circle(roi, extTop, 5, (0, 255, 0), 2)
        cv2.circle(roi, extBot, 5, (0, 255, 0), 2)

        cv2.line(roi, extLeft, extTop, (255, 0, 0), 2)
        cv2.line(roi, extTop, extRight, (255, 0, 0), 2)
        cv2.line(roi, extRight, extBot, (255, 0, 0), 2)
        cv2.line(roi, extBot, extLeft, (255, 0, 0), 2)

        a = math.sqrt((extRight[0] - extTop[0])**2 + (extRight[1] - extTop[1])**2)
        b = math.sqrt((extBot[0] - extRight[0]) ** 2 + (extBot[1] - extRight[1]) ** 2)
        c = math.sqrt((extBot[0] - extTop[0]) ** 2 + (extBot[1] - extTop[1]) ** 2)

        try:
            angle_ab = math.acos((a**2 + b**2 - c**2) / (2 * b * c)) * 57
            cv2.putText(roi, str(angle_ab), (extRight[0] - 100, extRight[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))

        except:
            cv2.putText(roi, '?', (extRight[0] - 100, extRight[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255))

    cv2.imshow('Frame', frame)
    cv2.imshow('Roi', roi)
    cv2.imshow('Mask', mask)

    key = cv2.waitKey(20)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
