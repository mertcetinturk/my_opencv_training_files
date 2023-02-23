import cv2

img = cv2.imread('contour1.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# bu iki değişken default olarak yazılır doğruluğu arttırmak için kullanılır

cv2.drawContours(image=img, contours=contours, contourIdx=1, color=(0, 0, 255), thickness=3)
# https://docs.opencv.org/4.x/d3/dc0/group__imgproc__shape.html#gae4156f04053c44f886e387cff0ef6e08

cv2.imshow('Contour', img)
cv2.waitKey(0)
cv2.destroyAllWindows()





