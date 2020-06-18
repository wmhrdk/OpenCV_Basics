import cv2
import numpy as np

""" DETECT CIRCLES IN IMAGE

img = cv2.imread('img/img_03.jpg', cv2.IMREAD_COLOR)
img_grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blurred = cv2.medianBlur(img_grayscaled, 5)

circles = cv2.HoughCircles(img_blurred, cv2.HOUGH_GRADIENT, 1, 20,\
                          param1=50, param2=30,\
                          minRadius=80, maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0, :]:
	center = (i[0], i[1])
	cv2.circle(img, center, 1, (255,0,0), 3)
	cv2.circle(img, center, i[2], (255,255,0), 3)

cv2.imshow('img', img)

cv2.waitKey(0)

"""

cap = cv2.VideoCapture(0)

while True:
	ret, frame = cap.read()

	frame_grayscaled = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	frame_blurred = cv2.medianBlur(frame_grayscaled, 5)
	#retval, threshold = cv2.threshold(frame_blurred, 10, 255, cv2.THRESH_BINARY)
	edges = cv2.Canny(frame_blurred, 60, 60)

	contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(frame, contours, -1, (255,100,0), 1)

	"""
	circles = cv2.HoughCircles(frame_blurred, cv2.HOUGH_GRADIENT, 1, 200,\
								param1=80, param2=30,\
								minRadius=80, maxRadius=0)

	circles = np.uint16(np.around(circles))
	for i in circles[0, :]:
		center = (i[0], i[1])
		cv2.circle(frame_blurred, center, 1, (255,0,0), 3)
		cv2.circle(frame_blurred, center, i[2], (255,255,0), 3)
	"""

	cv2.imshow('frame', frame)
	cv2.imshow('gray', frame_blurred)
	cv2.imshow('edges', edges)
	#cv2.imshow('tresh', threshold)
	#cv2.imshow('result', frame_blurred)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()