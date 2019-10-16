import cv2
import numpy as np

cap = cv2.VideoCapture(-1)

while True:
	_, frame = cap.read()
	#underscore is a value that is returned from a function (we don't care!)

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	#hue saturation value

	lower_blue = np.array([15,15,15])
	upper_blue = np.array([70, 120, 120])

	mask = cv2.inRange(hsv, lower_blue, upper_blue)
	#currently mask is identical to frame
	#mask is a boolean operation (either 0 or 1)

	res = cv2.bitwise_and(frame, frame, mask=mask)
	#in the frame, there is a frame, and the mask=mask
	#mask = 1 (in the range); white

	kernel = np.ones((15, 15), np.float32)/255
	#devide by 15 * 15
	#make a average 15 * 15 pixel

	smoothed = cv2.filter2D(res, -1, kernel)

	blur = cv2.GaussianBlur(res, (15, 15), 0)

	median = cv2.medianBlur(res, 15)

	bilateral = cv2.bilateralFilter(res, 15, 75, 75)

	cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('res', res)
	cv2.imshow('kernel', kernel)
	cv2.imshow('blur', blur)
	cv2.imshow('median', median)
	cv2.imshow('bilateral', median)

	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
cap.release()
#closes the camera