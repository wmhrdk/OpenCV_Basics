import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# hsv, hue, sat value
	lower_red = np.array([0,10,10])
	upper_red = np.array([7,255,255])

	mask = cv2.inRange(hsv, lower_red, upper_red)
	res = cv2.bitwise_and(frame, frame, mask = mask)

	# Simple Blur
	kernel = np.ones((15, 15), np.float32)/225
	sblur = cv2.filter2D(frame, -1, kernel)

	# Gaussian Blur
	#gblur = cv2.GaussianBlur(frame, (15, 15), 0)

	# Median Blur
	#mblur = cv2.medianBlur(frame, 15)

	# Bilateral Blur
	#bblur = cv2.bilateralFilter(frame, 15, 75, 75)

	cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('res', res)
	#cv2.imshow('sblur', sblur)
	#cv2.imshow('gblur', gblur)
	#cv2.imshow('mblur', mblur)
	#cv2.imshow('bblur', bblur)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()