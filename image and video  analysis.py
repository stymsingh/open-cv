import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()#ret returns true or false
    cv2.imshow('frame', frame)

    if cv2.waitkey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
