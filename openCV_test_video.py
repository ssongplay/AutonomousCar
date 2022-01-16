import numpy as np
import cv2

cap = cv2.VideoCapture("samples/play/sample1.mp4")

while True:
    _, frame=cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('real', frame)
    cv2.imshow('video', gray)

    if cv2.waitKey(100)&0xFF == 27:   #ESC를 누르면 종료
        break

cap.release()
cv2.destroyAllWindows()
