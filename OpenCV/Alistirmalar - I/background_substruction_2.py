import cv2

cap = cv2.VideoCapture('car.mp4')
subtructer = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=150, detectShadows=True)
# https://docs.opencv.org/4.x/d7/d7b/classcv_1_1BackgroundSubtractorMOG2.html

# subtructer = cv2.createBackgroundSubtractorKNN(history=100, dist2Threshold=255, detectShadows=True)
# https://docs.opencv.org/4.x/db/d88/classcv_1_1BackgroundSubtractorKNN.html

while True:

    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))

    mask = subtructer.apply(frame)  # Member Function Documentation

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)

    if cv2.waitKey(20) and 0xFF == ord('q'):

        break

cap.release()
cv2.destroyAllWindows()
