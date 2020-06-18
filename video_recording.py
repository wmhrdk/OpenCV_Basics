import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out_normal = cv2.VideoWriter('vids/output_normal.avi', fourcc, 24.0, (640, 480))
#out_grayscale = cv2.VideoWriter('vids/output_grayscale.avi', fourcc, 24.0, (640, 480))

while(True):

	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	out_normal.write(frame)
	#out_grayscale.write(gray)

	cv2.imshow('frame', frame)
	cv2.imshow('gray', gray)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
out_normal.release()
#out_grayscale.release()
cv2.destroyAllWindows()
