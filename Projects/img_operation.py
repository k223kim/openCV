import numpy as np
import cv2

oriimg = cv2.imread('/home/kaeun/Projects/grandma.JPG', cv2.IMREAD_COLOR)
img = cv2.resize(oriimg, None, fx=0.2, fy=0.2)

#modify pixel
img[55,55] = [255, 255, 255]

#how to reference specific pixel
px = img[55, 55]
#will return a color value of that pixel

# print(px)

#ROI: Region of Image (subimage)

roi = img[100:150, 100:150] = [255, 255, 255]

grandma_face = img[350:560, 200:280]
img[0:210, 0:80] = grandma_face

img[200:410, 400:480] = grandma_face
#must be the same size

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()