import cv2
import numpy as np

oriimg1 = cv2.imread('/home/kaeun/Projects/A.jpg')
img1 = cv2.resize(oriimg1, None, fx=0.4, fy=0.4)
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.3, 10)
#find up to 100 corners
#image quality = 0.01
#minimum distance between corners: 10

corners = np.int0(corners)
# print(corners)

for corner in corners:
	x, y = corner.ravel()
	cv2.circle(img1, (x,y), 3, 255, -1)

cv2.imshow('Corner', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

