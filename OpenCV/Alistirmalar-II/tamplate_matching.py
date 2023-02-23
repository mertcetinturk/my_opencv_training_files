import cv2
import numpy as np

img = cv2.imread('starwars.jpg')
template = cv2.imread('starwars2.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
(w, h) = gray_template.shape[::-1]

result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
location = np.where(result >= 0.95)

for point in zip(*location[::-1]):  # height ve width sırasıyla alsın diye -1 yazılıyor. default (h, w)
    cv2.rectangle(img, point, (point[0] + w, point[1] + h), (0, 255, 0), 3)

cv2.imshow('IMG', img)
cv2.waitKey(0)
cv2.destroyAllWindows()