import cv2
import numpy as np

img_bgr = cv2.imread('img/IMG_7401.jpg')
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

temp = cv2.imread('img/IMG_7401_Face1.jpg', 0)
w, h = temp.shape[::-1]

result = cv2.matchTemplate(img_gray, temp, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(result>=threshold)

for pt in zip(*loc[::-1]):
	cv2.rectangle(img_bgr, pt, (pt[0]+w, pt[1]+h), (255,150,25), 2)

cv2.imshow('detected', img_bgr)

cv2.waitKey(0)
cv2.destroyAllWindows()