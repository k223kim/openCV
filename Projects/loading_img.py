import cv2
import numpy as numpy
import matplotlib.pyplot as plt

oriimg = cv2.imread('/home/kaeun/Projects/grandma.JPG', cv2.IMREAD_GRAYSCALE)
#other options: 
#IMREAD_COLOR =1
#IMREAD_UNCHANGED -1 - 
#grayscale 0

# print(img.shape)

img = cv2.resize(oriimg, None, fx=0.2, fy=0.2)

# cv2.imshow('image', img)
# cv2.waitKey(0) #press any key
# cv2.destroyAllWindows()

#we would mostly use imshow

#save image
cv2.imwrite('grandmalove.png', img)

plt.imshow(img, cmap='gray', interpolation='bicubic')
#opencv: BGR, matplotlib: RGB
plt.plot([50, 100], [80, 100], 'c', linewidth=5)
# plt.savefig('demo.png', bbox_inches='tight')
plt.show()

