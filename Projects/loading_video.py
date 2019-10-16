import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#first webcam in the system: 0

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2. VideoWriter('output.avi', fourcc, 20.0, (640, 480))
#how to save the recorded file

while True:
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#convert the color
	#true or false and frame
	
	out.write(frame)

	cv2.imshow('frame', frame)
	cv2.imshow('gray', gray)

	#how to get out of the loop
	if cv2.waitKey(1) & 0xFF == ord('q'):
		#if the key is equal to q
		break

cap.release()
#releases the capture/camera (saving a file)
out.release()

cv2.destroyAllWindows()