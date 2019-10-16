import cv2
import numpy as np
import matplotlib.pyplot as plt

oriimg = cv2.imread('/home/kaeun/Projects/dad.JPG')
img = cv2.resize(oriimg, None, fx=0.4, fy=0.4)
mask = np.zeros(img.shape[:2], np.uint8)
#uint8 is the datatype

bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)

rect = (270, 400, 360, 940)
#this is the coordinates of a rectangle which includes the foreground object in the format (x,y,w,h)


cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2) | (mask==0), 0, 1).astype('uint8')
#(0 or 2) or (1 or 3)

img = img*mask2[:,:,np.newaxis]


newimg = cv2.imread('/home/kaeun/Projects/dad_edited.JPG')
newmask = cv2.resize(newimg, None, fx=0.4, fy=0.4)

mask[newmask == 0] = 0
mask[newmask == 255] = 1

mask, bgdModel, fgdModel = cv2.grabCut(img, mask, None, bdgModel, fgdModel, 5, cv2.GC_INIT_WITH_MASK)
mask = np.where((mask==2) | (mask==0), 0, 1).astype('uint8')
img = img*mask[:,:,np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()