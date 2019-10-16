import cv2
import numpy as np

oriimg_bgr = cv2.imread('/home/kaeun/Projects/grandma_roll.jpg')
img_bgr = cv2.resize(oriimg_bgr, None, fx=0.4, fy=0.4)
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

oritemplate = cv2.imread('/home/kaeun/Projects/roll.png', 0)
template = cv2.resize(oritemplate, None, fx=0.2, fy=0.2)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res >= threshold)

#mark on actual pictures (yellow rectangle)
for pt in zip(*loc[::-1]):
	cv2.rectangle(img_bgr, pt, (pt[0] + w, pt[1]+ h), (0, 255, 255), 2)

cv2.imshow('detected', img_bgr)

cv2.waitKey(0)
cv2.destroyAllWindows()