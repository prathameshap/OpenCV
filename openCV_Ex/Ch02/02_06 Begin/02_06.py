#02_06 Begin

#! /usr/bin/env python3


import numpy as np
import cv2

#loading of image
image = cv2.imread("thresh.jpg")
cv2.imshow("Original", image)

blur = cv2.GaussianBlur(image, (5,55),0) #values in the bracket have to be odd
cv2.imshow("Blur",blur)

kernel = np.ones((5,5),'uint8')

#dilation filter
dilate = cv2.dilate(image, kernel, iterations=1)
#erosion filter
erode = cv2.erode(image,kernel,iterations=1)

cv2.imshow("Dilate", dilate)
cv2.imshow("Erode",erode)

cv2.waitKey(0)
cv2.destroyAllWindows()
