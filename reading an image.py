import numpy as np
import cv2
import matplotlib.pyplot as plt

# open cv code

img = cv2.imread('index.jpg',0)
cv2.imshow('image',img)
k = cv2.waitKey(0)#wait for any key to be pressed
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()
