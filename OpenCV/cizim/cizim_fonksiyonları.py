import numpy as np
import cv2

canvas = np.zeros((512, 512, 3), dtype = np.uint8) + 255

cv2.line(canvas, (50, 50), (512, 512), color=(255, 0, 0), thickness=5)

cv2.rectangle(img=canvas, pt1=(50, 50), pt2= (400, 400), color=(0,255,0), thickness=10, lineType=None, shift=None)

cv2.circle(img=canvas, center=(256,256), radius= 100, color=(255, 0, 255), thickness=5)

# üçgen için özel bir fonksiyon olmadığından düz çizgileri birleştirerek üçgen oluşturulabilir

points = np.array([[[110, 200], [330, 200], [290, 220], [100, 100]]], np.int32)

cv2.polylines(img=canvas, pts=points, isClosed=True, color=(255,255, 0), thickness=5)

cv2.ellipse(img=canvas, center=(256, 256), axes=(100, 50), angle=98.2, startAngle=0, endAngle=360, color=(0,0,0), thickness=8)

cv2.imshow('Canvas', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()