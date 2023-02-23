import cv2

window_name = 'Laplacian Demo'
ddepth = cv2.CV_16S
kernel_size = 3


img = cv2.imread('starwars.jpg')
blurry_img = cv2.medianBlur(img, 7)

# laplacian = cv2.Laplacian(blurry_img, cv2.CV_64F).var()  burada blurluk var mı yok mu onu kontrol ediyoruz

gray = cv2.cvtColor(blurry_img, cv2.COLOR_BGR2GRAY)

cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

lap = cv2.Laplacian(gray, ddepth, kernel_size)  # burada laplacian filter uyguluyoruz
# https://docs.opencv.org/3.4/d5/db5/tutorial_laplace_operator.html

abs_dst = cv2.convertScaleAbs(lap)

cv2.imshow(window_name, abs_dst)

cv2.imshow('img', img)
cv2.imshow('blur', blurry_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
