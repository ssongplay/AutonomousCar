import cv2
import numpy as np

img = cv2.imread("samples/image/sample3.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=35, minRadius=0, maxRadius=0)
circles = np.uint16(np.around(circles))

for c in circles[0, :]:
    center = (c[0], c[1])
    radius = c[2]

    #cv2.circle(img, center, radius, (0, 255, 0), 2) # green
    cv2.circle(img, center, radius, (0, 0, 255), 3) # red

cv2.imshow('result', img)

if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()