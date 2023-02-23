import cv2
import numpy as np

img = cv2.imread('klon.jpg', 0)
kernel = np.ones((5, 5), np.uint8)
# erosion = cv2.erode(img, kernel=kernel, iterations=1)  # resmi inceltiyor
# cv2.imshow('erosion', erosion)

# dilation = cv2.dilate(img, kernel=kernel, iterations=5)  # resmi kalınlaştırıyor
# cv2.imshow('dilation', dilation)

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel=kernel)  # resimdeki noise ları kaldırıyor
cv2.imshow('opening', opening)
#
close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel=kernel)  # resmin içindeki noise ları kaldırıyor
cv2.imshow('close', close)

# gradiant = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel=kernel)  # resmin dış kısmını vurguluyor
# cv2.imshow('gradiant', gradiant)

'''
### cv2.MORPH_TOPHAT ve cv2.MORPH_BLACKHAT fonksiyonları da yazıyı/objeyi silmeye yarıyor
### cv2.MORPH_TOPHAT harflerin birleşim yerlerini siliyor
'''

cv2.waitKey(0)
cv2.destroyAllWindows()
