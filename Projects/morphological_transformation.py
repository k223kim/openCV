import cv2
import numpy as np

cap = cv2.VideoCapture(-1)

while True:
	_, frame = cap.read()

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	lower_blue = np.array([15,15,15])
	upper_blue = np.array([70, 120, 120])

	mask = cv2.inRange(hsv, lower_blue, upper_blue)

	res = cv2.bitwise_and(frame, frame, mask=mask)

	#erosion: slider slides around and if all the pixels are identical, it moves on
	#if not all pixels are not identical, it will remove that different pixel

	kernel = np.ones((3,3), np.uint8)
	erosion = cv2.erode(mask, kernel, iterations = 1)

	#dilation: it pushes out the pixel until it cannot
	dilation = cv2.dilate(mask, kernel, iterations = 1)

	#opening: remove false positives (remove stuff (noise) in the background)
	opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

	#closing: remove false negatives (remove noise in the hat)
	closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

	#tophat: difference between the input image and the Opening of the image
	# cv2.imshow('Tophat', tophat)

	#blackhat: difference between the closing of the input image and input image
	# cv2.imshow('Blackhat', blackhat)


	cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('opening', opening)
	cv2.imshow('closing', closing)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
cap.release()
#closes the camera