import cv2
import numpy as np

oriimg1 = cv2.imread('/home/kaeun/Projects/mom.JPG')
img1 = cv2.resize(oriimg1, None, fx=0.2, fy=0.2)
oriimg2 = cv2.imread('/home/kaeun/Projects/grandma.JPG')
img2 = cv2.resize(oriimg2, None, fx=0.2, fy=0.2)

# add = img1 + img2

# add = cv2.add(img1, img2)
#added all the pixel values
#e.g. (155, 211, 79) + (50, 170, 200) = (205, 381, 279).. translated to (205, 255, 255)

# weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
#img1 weight is 0.6


# cv2.imshow('weight', weighted)

oriimg3 = cv2.imread('/home/kaeun/Projects/panda.jpg')
img3 = cv2.resize(oriimg3, None, fx=0.1, fy=0.1)

rows, cols, channels = img3.shape
roi = img1[0:rows, 0:cols]

img3gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img3gray, 60, 255, cv2.THRESH_BINARY_INV)
# 220 is the threshold value
#if pixel value is above 220, it will be converted to 255
#if pixel value is above 220, it will be black
#and convert those! THRESH_BINARY_INV

# cv2.imshow('mask', mask)

mask_inv = cv2.bitwise_not(mask)
# #black area (invisible part)
# #bitwise is just like python logical operations
#where mask is not a value i.e. 255

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
# #or is like and-or
#xor means only one of these (never both)

img3_fg = cv2.bitwise_and(img3, img3, mask=mask)

dst = cv2.add(img1_bg, img3_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img1)
cv2.imshow('mask_inv', mask_inv)
cv2.imshow('img1_bg', img1_bg)
cv2.imshow('img3_fg', img3_fg)
cv2.imshow('dst', dst)
cv2.imshow('im3', img3)
cv2.imshow('mask', mask)


cv2.waitKey(0)
cv2.destroyAllWindows()