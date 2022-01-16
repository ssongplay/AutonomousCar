# 특정색 추출 (HSV 정보에서 추출)
import numpy as np
import cv2
range = 18
def tracking():
    cap = cv2.VideoCapture(0)
    lower_blue = np.array([120-range, 20, 20])
    upper_blue = np.array([120+range, 255, 255])
    lower_green = np.array([60-range, 20, 20])
    upper_green = np.array([60+range, 255, 255])
    lower_red = np.array([-range, 60, 60])
    upper_red = np.array([range, 255, 255])

    while True:
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        blue_range = cv2.inRange(hsv, lower_blue, upper_blue)
        green_range = cv2.inRange(hsv, lower_green, upper_green)
        red_range = cv2.inRange(hsv, lower_red, upper_red)
        blue_result = cv2.bitwise_and(frame, frame, mask=blue_range)
        red_result = cv2.bitwise_and(frame, frame, mask=red_range)
        green_result = cv2.bitwise_and(frame, frame, mask=green_range)

        cv2.imshow("original", frame)
        cv2.imshow("blue", blue_result)
        cv2.imshow("red", red_result)
        cv2.imshow("green", green_result)

        key = cv2.waitKey(1) & 0xFF
        if key == 27:
            break
    cv2. destroyAllWindows()
tracking()
