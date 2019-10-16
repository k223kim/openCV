import cv2
import numpy as np

oriimg = cv2.imread('/home/kaeun/Projects/kajin.JPG')
img = cv2.resize(oriimg, None, fx=0.5, fy=0.5)

retval, threshold = cv2.threshold(img, 105, 255, cv2.THRESH_BINARY)
#above 12, it will be white
#below 12, will be black

grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled, 105, 255, cv2.THRESH_BINARY)
retval3, otsu = cv2.threshold(grayscaled, 125, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 3, 1)
#255 is the max value assigned to the pixel
#3 is the block size which are used to calculate a threshold value
#1 is the weighted mean

gaus2 = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow('original', img)
cv2.imshow('threshold', threshold)
# cv2.imshow('threshold2', threshold2)
cv2.imshow('gaus', gaus)
# cv2.imshow('otsu', otsu)
cv2.imshow('gaus2', gaus2)
cv2.waitKey(0)
cv2.destroyAllWindows()