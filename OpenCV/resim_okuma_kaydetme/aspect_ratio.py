import cv2

def resizewithAspectRatio(img, witdh = None, height = None, inter = cv2.INTER_AREA):

    dimension = None

    (h,w) = img.shape[:2]

    if witdh is None and height is None:
        return img

    if witdh is None:
        r = height / float(h)
        dimension = (int(w * r), height)

    else:
        r = witdh / float(w)
        dimension = (witdh, int(h * r))

    return cv2.resize(img, dimension, interpolation = inter)

img = cv2.imread('klon.jpg')
img1 = resizewithAspectRatio(img, witdh = None, height = 600, inter = cv2.INTER_AREA)

cv2.imshow('Orijinal', img)
cv2.imshow('Resized', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()