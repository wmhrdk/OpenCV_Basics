import cv2
import numpy as np

# default color range variables
lowHue = 0; lowSat = 100; lowVal = 100
highHue = 15; highSat = 255; highVal = 255

def nothing(*arg):
	pass

# Create Trackbar
cv2.namedWindow('colorPick')
# Lower range colour sliders.
cv2.createTrackbar('lowHue', 'colorPick', lowHue, 255, nothing)
cv2.createTrackbar('lowSat', 'colorPick', lowSat, 255, nothing)
cv2.createTrackbar('lowVal', 'colorPick', lowVal, 255, nothing)
# Higher range colour sliders.
cv2.createTrackbar('highHue', 'colorPick', highHue, 255, nothing)
cv2.createTrackbar('highSat', 'colorPick', highSat, 255, nothing)
cv2.createTrackbar('highVal', 'colorPick', highVal, 255, nothing)

# Capture frame from camera
cap = cv2.VideoCapture(0)

# Infinite looping
while True:
	_, frame = cap.read()

	# Convert frame's color from BGR to HSV
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# Get color range value from trackbars
	lowHue = cv2.getTrackbarPos('lowHue', 'colorPick')
	lowSat = cv2.getTrackbarPos('lowSat', 'colorPick')
	lowVal = cv2.getTrackbarPos('lowVal', 'colorPick')
	highHue = cv2.getTrackbarPos('highHue', 'colorPick')
	highSat = cv2.getTrackbarPos('highSat', 'colorPick')
	highVal = cv2.getTrackbarPos('highVal', 'colorPick')

	# Put lower and upper color values into one variable using np array
	# hsv color = hue, sat, value
	lower_color = np.array([lowHue, lowSat, lowVal])
	upper_color = np.array([highHue, highSat, highVal])

	# Apply median blur to frame for noise reduction
	blurred = cv2.medianBlur(hsv, 5)

	# Apply mask to frame
	mask = cv2.inRange(blurred, lower_color, upper_color)

	# Apply erosion and dilation to frame
	kernel = np.ones((5,5), np.uint8)
	erosion = cv2.erode(mask, kernel, iterations = 3)
	dilation = cv2.dilate(erosion, kernel, iterations = 2)

	# Show result
	res = cv2.bitwise_and(frame, frame, mask = dilation)

	# Apply Canny edge detection to frame
	edges = cv2.Canny(dilation, 130, 130)
	
	# Find contours in the frame
	contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	if len(contours) != 0:
	    # Draw the contours that were founded
	    cv2.drawContours(frame, contours, -1, (255,100,0), 3)

	    # Find the biggest area
	    c = max(contours, key = cv2.contourArea)

	    # Get x, y position and width, height of the largest contour
	    x,y,w,h = cv2.boundingRect(c)

	    # Draw rectangle on the biggest contour
	    cv2.rectangle(frame, (x,y), (x+w,y+h), (50,250,0), 2)

	    # Set center positon and the distance from camera
	    centerX = x + (w / 2)
	    centerY = y + (h / 2)
	    centerZ = (10 * 315) / w

	    # Put texts into the frame
	    cv2.putText(frame, ('x='+str(centerX)), ((x+w)+10, y+10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (110,60,255), 2, cv2.LINE_AA)
	    cv2.putText(frame, ('y='+str(centerY)), ((x+w)+10, y+30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,60,110), 2, cv2.LINE_AA)
	    cv2.putText(frame, ('z='+str(centerZ)), ((x+w)+10, y+50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,60,255), 2, cv2.LINE_AA)
	    cv2.putText(frame, ('w='+str(w)), (x, (y+h)+30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (50,250,0), 2, cv2.LINE_AA)

	# Get frame width and height
	fwidth = cap.get(3)
	fheight = cap.get(4)

	# Show frame width and height on the frame
	cv2.putText(frame, ('fw='+str(fwidth)), (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (50,250,250), 2, cv2.LINE_AA)
	cv2.putText(frame, ('fh='+str(fheight)), (10,40), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (50,250,250), 2, cv2.LINE_AA)

	"""Show Frame"""
	cv2.imshow('frame', frame)
	#cv2.imshow('mask', mask)
	cv2.imshow('res', res)
	#cv2.imshow('erosion', erosion)
	cv2.imshow('dilation', dilation)
	cv2.imshow('edges', edges)
	#cv2.imshow('thresholded', thresholded)

	# Get Esc key to break from infinite loop
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()