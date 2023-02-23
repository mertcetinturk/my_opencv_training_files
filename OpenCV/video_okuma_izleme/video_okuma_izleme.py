import cv2

# webcamden kullanacaksan 0 değerini gireceğiz kamera kullanacaksak 1-2 gibi değerler kullanıcaz
cap = cv2.VideoCapture('antalya.mp4')  # soruce reader cv2 tarzında bir hata alınırsa 0 dan sonra , cv2.CAP_DSHOW flagini girersek hatadan kurtuluruz

while True:
    ret, frame = cap.read()  # ret değişkeni True False değerini alır
    if ret == 0:
        break

    frame = cv2.flip(frame, 1)  # y eksenine göre yansıtılır

    cv2.imshow('Antalya', frame)

    # milisaniye değeri
    # 0xFF == ord('q') un anlamı klavyeden q harfine bastığımda frame'i kapat demektir.
    # ord fonksiyonuyla klavyeye bağlanır.
    # 0xFF makine dilinde kapat demektir

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
