import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

filename = 'C:\Users\Mert\OneDrive\Masaüstü\OpenCV\webcam.avi'
codec = cv2.VideoWriter_fourcc('W', 'M', 'V', '2')  #media verilerindeki codecleri 4 karakterle tanımlar
# wmv2 	Windows Media Video 8 codec
#https://softron.zendesk.com/hc/en-us/articles/207695697-List-of-FourCC-codes-for-video-codecs
# FourCC codes for video codecs

frameRate = 30
resolution = (640, 480)

videoFileOutput = cv2.VideoWriter(filename, codec, frameRate, resolution)

while True:
    ret, frame = cap.read()
    cv2.flip(frame, 1)
    videoFileOutput.write(frame)

    cv2.imshow('Webcam Live', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

videoFileOutput.release()
cap.release()
cv2.destroyAllWindows()