import cv2

cap = cv2.VideoCapture('car.mp4')

circles = []


def mouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        circles.append((x, y))


cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame', mouse)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))

    for center in circles:
        cv2.circle(frame, center, 20, (0, 0, 255), -1)

    cv2.imshow('Frame', frame)

    key = cv2.waitKey(20)

    if key == 27:
        break

    elif key == ord('h'):
        circles = []

cap.release()
cv2.destroyAllWindows()
