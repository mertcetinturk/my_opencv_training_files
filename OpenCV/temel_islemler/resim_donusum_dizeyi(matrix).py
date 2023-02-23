import cv2
import numpy as np

img = cv2.imread('klon.jpg', 0)
row, col = img.shape

x = 10
y =  70

M = np.float32([[1, 0, x], [0, 1, y]])
dst = cv2.warpAffine(img, M, (row, col))

cv2.imshow('Original', img)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()