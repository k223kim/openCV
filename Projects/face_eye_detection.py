#using Haar Cascade

import cv2
import numpy as np

# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

myface_cascade = cv2.CascadeClassifier('cascade.xml')

cap = cv2.VideoCapture(-1)

while True:
	ret, img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	# # 1.3 the likelihood that you might find, size of the object
	# for (x, y, w, h) in faces:
	# 	cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
	# 	#(x, y) is starting point
	# 	#(x+w, y+h) is ending point
	# 	roi_gray = gray[y:y+h, x:x+w]
	# 	#region (y starting, y ending, x starting, x ending)
	# 	roi_color = img[y:y+h, x:x+w]
	# 	eyes = eye_cascade.detectMultiScale(roi_gray)
	# 	#since eye is always within the region of the face
	# 	for (ex, ey, ew, eh) in eyes:
	# 		cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
	faces = myface_cascade.detectMultiScale(gray, 1.3, 5)
	# 1.3 the likelihood that you might find, size of the object
	for (x, y, w, h) in faces:
		cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
		#(x, y) is starting point
		#(x+w, y+h) is ending point
		# roi_gray = gray[y:y+h, x:x+w]
		# #region (y starting, y ending, x starting, x ending)
		# roi_color = img[y:y+h, x:x+w]
		# eyes = eye_cascade.detectMultiScale(roi_gray)
		# #since eye is always within the region of the face
		# for (ex, ey, ew, eh) in eyes:
		# 	cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

	cv2.imshow('img',img)
	k = cv2.waitKey(10) & 0xff
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()
