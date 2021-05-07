import cv2
import numpy as np
import pdb


img = cv2.imread('escorpiao.png')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

## mask of green (36,25,25) ~ (86, 255,255)
#Red color rangle  169, 100, 100 , 189, 255, 255

lower_range = np.array([50,252,252])
upper_range = np.array([185, 255,252])

# lower_range = np.array([40, 40,40])
# upper_range = np.array([70,255,255])

mask = cv2.inRange(hsv, lower_range, upper_range)

if cv2.countNonZero(mask) > 0:
    print('Escorpion is present!')
else:
    print('Escorpion is not present!')

cv2.imshow('image', img)
cv2.imshow('mask', mask)

cv2.waitKey(0)
cv2.destroyAllWindows()
# img = cv2.imread('escorpiao.png') 
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
