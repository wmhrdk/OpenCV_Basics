import numpy as numpy
import cv2

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out_normal = cv2.VideoWriter('vids/output_normal.avi', fourcc, 24.0, (640, 480))

while(True):

    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    for(x, y, w, h) in faces:
        print(x, y, w, h)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    out_normal.write(frame)
    
    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out_normal.release()
cv2.destroyAllWindows()