import cv2
import numpy as np

img1 = cv2.imread('aircraft.jpg')
img1 = cv2.resize(img1, (640, 550))

img2 = cv2.imread('aircraft1.jpg')
img2 = cv2.resize(img2, (640, 550))

if img1.shape == img2.shape:
    print('Same Size')
else:
    print('NOT Same Size')

# genelde bu değişken adı kullanılır diff --> differance
diff = cv2.subtract(img1, img2)  # aynı olan yerleri siyaha boyar
b, g, r = cv2.split(diff)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)

if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
    print('Completely Equal')

else:
    print('NOT Completely Equal')

cv2.waitKey(0)
cv2.destroyAllWindows()