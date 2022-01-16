import cv2
import numpy as np

img = cv2.imread("samples/image/sample6.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blur, 50, 150, None, 3)
lines = cv2.HoughLines(edges, 1, np.pi/180, 100)
# HoughLines의 변수
# 1 : r-theta 좌표 상에서 r값 (0~1)
# np.pi/180: 각도를 삼각함수로 계산하기 위해 라디안 각으로 변환
# 100 : threshold 값으로 숫자가 작으면 많은 선이 검출되지만 정확도가 떨어짐

for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 1)

cv2.imshow('edges', edges)
cv2.imshow('result', img)
cv2.waitKey()
cv2.destroyAllWindows()