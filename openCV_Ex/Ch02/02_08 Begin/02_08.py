##This file takes input from camera and resizes every frame and shows 
#process terminates if user presses 'q'

import numpy as np
import cv2

#Accessing the camera
cap = cv2.VideoCapture(0)

while(True):

    ret, frame = cap.read()

    frame = cv2.resize(frame, (0,0), fx=0.5,fy=0.5)
    cv2.imshow("Frame",frame)


    ch = cv2.waitKey(1)
    #0xFF is needed only on 64 bit machine
    if ch & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
