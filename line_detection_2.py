import cv2
import numpy as np

img = cv2.imread("samples/image/sample6.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blur, 50, 150, None, 3)
lines = cv2.HoughLinesP(edges, 2, np.pi/180, 20, minLineLength=10, maxLineGap=5)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0,0,0), 3)

cv2.imshow('edges', edges)
cv2.imshow('result', img)

cv2.waitKey()
cv2.destroyAllWindows()