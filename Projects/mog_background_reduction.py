#find changes and note that as foreground
#don't change is background
#more close to 'non-action-motion'

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture('/home/kaeun/Projects/output.avi')
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
	rst, frame = cap.read()
	fgmask = fgbg.apply(frame)

	cv2.imshow('original', frame)
	cv2.imshow('fg', fgmask)

	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()
