import cv2
import numpy as np

img = cv2.imread('h_line.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 75, 150)

# cv2.HoughLines() çok fazla cpu kullanıyor

lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, minLineLength=None, maxLineGap=170)  # opencv de default olarak verilen değerler: img, rho (uzaklık), theta (açı), threshold

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow('img', img)
cv2.imshow('edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
