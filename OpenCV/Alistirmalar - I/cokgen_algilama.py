import cv2
import numpy as np

font = cv2.FONT_HERSHEY_SIMPLEX
font1 = cv2.FONT_HERSHEY_COMPLEX

img = cv2.imread('polygons.png')
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(grey, 240, 255, cv2.THRESH_BINARY)

contour, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contour:
    epsilon = 0.01 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(curve=cnt, epsilon=epsilon, closed=True)

    cv2.drawContours(img, [approx], 0, (0, 0, 255), 3)

    x = approx.ravel()[0]
    y = approx.ravel()[1]

    # x, y = approx[0][0]   bu şekilde de yazılabilir

    if len(approx) == 3:
        cv2.putText(img, 'Triangle', (x, y), font, 1, (0, 0, 0))
    elif len(approx) == 4:
        cv2.putText(img, 'Rectangle', (x, y), font, 1, (0, 0, 0))
    elif len(approx) == 5:
        cv2.putText(img, 'Pentagon', (x, y), font, 1, (0, 0, 0))
    elif len(approx) == 6:
        cv2.putText(img, 'Hexagon', (x, y), font, 1, (0, 0, 0))
    else:
        cv2.putText(img, 'Ellipse', (x, y), font, 1, (0, 0, 0))

cv2.imshow('IMG', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
