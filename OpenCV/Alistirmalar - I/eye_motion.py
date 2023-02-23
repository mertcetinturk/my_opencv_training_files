import cv2

vid = cv2.VideoCapture('eye_motion.mp4')

while True:
    ret, frame = vid.read()
    if ret is False:
        break

    else:
        roi = frame[80:210, 230:450]

        # scale_percent = 160  # %160
        # width = int(roi.shape[1] * scale_percent / 100)
        # height = int(roi.shape[0] * scale_percent / 100)
        # dim = (width, height)
        # roi = cv2.resize(roi, dim, interpolation=cv2.INTER_AREA)

        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

        ret, thresh = cv2.threshold(gray, 3, 255, cv2.THRESH_BINARY_INV)

        rows, cols, channel = roi.shape

        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(roi, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.line(roi, (x + int(w / 2), 0), (x + int(w / 2), rows), (0, 255, 0), 2)
            cv2.line(roi, (0, y + int(h / 2)), (cols, y + int(h / 2)), (0, 255, 0), 2)
            break

        frame[80:210, 230:450] = roi  # roi frame inin boyutunu değiştirdiysen eski boyutuna geri getirmelisin

        cv2.imshow('frame', frame)
        cv2.imshow('roi', roi)

        key = cv2.waitKey(80)

        if key == 27:
            break

vid.release()
cv2.destroyAllWindows()
