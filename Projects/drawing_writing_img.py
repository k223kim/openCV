import numpy as np
import cv2

oriimg = cv2.imread('/home/kaeun/Projects/grandma.JPG', cv2.IMREAD_COLOR)

img = cv2.resize(oriimg, None, fx=0.2, fy=0.2)
cv2.line(img, (0,0), (150,150), (255, 255, 255), 15)
#where do you want the line? 
#where does it start? where does it end?
#color
#line width

cv2.rectangle(img, (15, 25), (200, 150), (0, 255, 0), 5)
cv2.circle(img, (100, 63), 55, (0, 0, 255), -1)
#center, radius, color, line-width(-1 will fill in the circle)

pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
#np.int32 is the datatype

# pts = pts.reshape((-1, 1, 2))

cv2.polylines(img, [pts], True, (0, 255, 255), 3)
#true: do you want to connect the final point to the starting point? yes


#how to write
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV Tuts!', (0,130), font, 1, (200, 255, 255), 2, cv2.LINE_AA)
#where is the test?
#what are you going to write?
#where does it start?
#font?
#size?
#color?
#thickness


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#opencv: BGR
#if you want something totally blue: 255, 0,0
#if you want something white: 255, 255, 255
#if you want something black: 0, 0, 0
