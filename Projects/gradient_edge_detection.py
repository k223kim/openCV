import cv2
import numpy as np

cap = cv2.VideoCapture(-1)

while True:
	_, frame = cap.read()

	laplacian = cv2.Laplacian(frame, cv2.CV_64F)
	#cv2.CV_64F is the datatype
	sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize = 5)
	sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize = 5)

	#edge detector
	edges = cv2.Canny(frame, 80, 80)
	#100 * 200

	cv2.imshow('original', frame)
	cv2.imshow('laplacian', laplacian)
	cv2.imshow('edges', edges)
	cv2.imshow('sobely', sobely)


	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
cap.release()
#closes the camera