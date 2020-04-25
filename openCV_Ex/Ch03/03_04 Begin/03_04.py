import numpy as np
import cv2

img = cv2.imread('faces.jpeg',1)

#grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

h = hsv[:,:,0] #use all the hue values 
s = hsv[:,:,1] #use all the satuaration channels
v = hsv[:,:,2] #use all the channel values

hsv_split = np.concatenate((h,s,v), axis=1)
cv2.imshow("Split HSV", hsv_split)

ret, min_sat = cv2.threshold(s,40,255, cv2.THRESH_BINARY)

ret, max_hue = cv2.threshold(h,15,255, cv2.THRESH_BINARY_INV)
cv2.imshow("Hue Filter", max_hue)

final = cv2.bitwise_and(min_sat, max_hue)
cv2.imshow("Final", final)
cv2.imshow("Original", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
