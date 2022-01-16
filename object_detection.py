import cv2

img = cv2.imread("samples/image/sample2-1.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, 0)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# 원하는 이미지에 contour로 나뉜 구역을 표시
for cnt in contours:
    cv2.drawContours(img, [cnt], 0, (255, 0, 0), 3)
    area = cv2.contourArea(cnt)
    print(area)
cv2.imshow('result1', img)


# contour의 라인이 볼록한지 볼록하지 않은지를 판단하고 그 선을 볼록하고 평평한 선들로 이어주는 함수
for cnt in contours:
    cv2.drawContours(img, [cnt], 0, (255, 0, 0), 3)
    hull = cv2.convexHull(cnt)
    cv2.drawContours(img, [hull], 0, (255, 0, 255), 5)
cv2.imshow('result2', img)



# 해당 contour 영역의 모멘트(무게중심) 정보를 return
for cnt in contours:
    cv2.drawContours(img, [cnt], 0, (255, 0, 0), 3)
    M = cv2.moments(cnt)
    cx = int(M['m10'] / M['m00'])
    cy = int(M['m01'] / M['m00'])
    cv2.circle(img, (cx, cy), 10, (0, 0, 255), -1)
cv2.imshow('result3', img)


if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()