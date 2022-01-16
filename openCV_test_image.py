import cv2
print(cv2.__version__)

image = cv2.imread("samples/image/sample1.jpg", cv2.IMREAD_UNCHANGED)
cv2.namedWindow("Moon", cv2.WINDOW_NORMAL)
cv2.imshow("Moon", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

