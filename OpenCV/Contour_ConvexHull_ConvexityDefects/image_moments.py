import cv2

img = cv2.imread('contour.png')
gray = (cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))

ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

M = cv2.moments(thresh)

X = int(M['m10'] / M['m00'])  # burası opencv tutorial'ında da böyle
Y = int(M['m01'] / M['m00'])  # burası opencv tutorial'ında da böyle
# ağırlık merkezinin koordinatlarını bulmamızı sağlıyor
# https://docs.opencv.org/3.4/d0/d49/tutorial_moments.html

cv2.circle(img, (X, Y), 5, (0, 0, 255), -1)


cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
