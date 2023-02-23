import cv2
import numpy as np

img = cv2.imread('klon.jpg')

dimension = img.shape
print(dimension)

color = img[150, 200]
print('BGR:', color)

blue = img[150, 200, 0]
print('Blue:', blue)

green = img[150, 200, 1]
print('Green:', green)

red = img[150, 200, 2]
print('Red:', red)

img[150, 200, 0] = 250
print('New Blue:', img[150, 200, 0])


blue1 = img.item(150, 200, 0)
print('blue1',blue1)
img.itemset((150, 200, 0), 172)
print('new blue1',img[150, 200, 0])


cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
