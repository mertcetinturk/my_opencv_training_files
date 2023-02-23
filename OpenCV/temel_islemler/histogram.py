from matplotlib import pyplot as plt
import numpy as np
import cv2

img = np.zeros((512,512), np.uint8)
cv2.imshow('img', img)

plt.hist(img.ravel(), 256, (0, 256), color='purple')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()