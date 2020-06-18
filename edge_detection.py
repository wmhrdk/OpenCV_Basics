import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()

	# Canny edge detection
	edges = cv2.Canny(frame, 130, 130)

	cv2.imshow('normal', frame)
	cv2.imshow('edges', edges)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()