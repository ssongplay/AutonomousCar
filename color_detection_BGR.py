# 특정색 추출 (BGR 정보에서 추출)
import numpy as np
import cv2
def tracking():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        blue_result, green_result, red_result = cv2.split(frame)
        zeros = np.zeros((frame.shape[0], frame.shape[1]), dtype='uint8')
        blue_result = cv2.merge([blue_result, zeros, zeros])
        green_result = cv2.merge([zeros, green_result, zeros])
        red_result = cv2.merge([zeros, zeros, red_result])
        cv2.imshow("original", frame)
        cv2.imshow("blue", blue_result)
        cv2.imshow("red", red_result)
        cv2.imshow("green", green_result)
        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            break
    cv2. destroyAllWindows()
tracking()
