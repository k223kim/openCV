import cv2
import numpy as np
import matplotlib.pyplot as plt
#the template in the image can have differne light, image, etc

img1 = cv2.imread('/home/kaeun/Projects/tico.jpg', 0)
img2 = cv2.imread('/home/kaeun/Projects/mom.JPG', 0)

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)


bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

matches = bf.match(des1, des2)
matches = sorted(matches, key = lambda x:x.distance)
#sort them to most likely to match to least likely to match

img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:2], None, flags=2)
#match 30
plt.imshow(img3)
plt.show()