# 크기가 다른 원 검출
import cv2
import numpy as np

img = cv2.imread("samples/image/sample3-1.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)

while True:
    circles1 = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 50, param1=50, param2=35, minRadius=0, maxRadius=100)
    circles1 = np.uint16(np.around(circles1))

    for c in circles1[0, :]:
        center = (c[0], c[1])
        radius = c[2]

        cv2.circle(img, center, radius, (0, 255, 0), 2)
        cv2.circle(img, center, radius, (0, 0, 255), 3)

    circles2 = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 50, param1=50, param2=35, minRadius=100, maxRadius=200)
    circles2 = np.uint16(np.around(circles2))

    for c in circles2[0, :]:
        center = (c[0], c[1])
        radius = c[2]

        cv2.circle(img, center, radius, (0, 255, 0), 2)
        cv2.circle(img, center, radius, (0, 255, 0), 3)

    circles3 = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 50, param1=50, param2=35, minRadius=200, maxRadius=300)
    circles3 = np.uint16(np.around(circles3))

    for c in circles3[0, :]:
        center = (c[0], c[1])
        radius = c[2]

        cv2.circle(img, center, radius, (0, 255, 0), 2)
        cv2.circle(img, center, radius, (255, 0, 0), 3)

    cv2.imshow('result', img)

    if cv2.waitKey(0) & 0xFF == 27:
        break

cv2.destroyAllWindows()