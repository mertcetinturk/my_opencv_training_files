import cv2
import numpy as np

canvas = np.zeros((512, 512, 3), dtype=np.uint8) + 255

font1 = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(img=canvas, text='OpenCV', org=(150, 100), fontFace=font1, fontScale=2, color=(0, 0, 255))
# org metnin koordinatı (başlayacağı sol alt köşe)


cv2.imshow('Canvas', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
