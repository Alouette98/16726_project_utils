import cv2
import numpy as np

# load image
img = cv2.imread("./input.jpg")

cv2.imshow("img", img)

# convert to hsv
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

# threshold using inRange
range1 = (20,20,20)
range2 = (255,255,255)
mask = cv2.inRange(hsv,range1,range2)

# apply morphology closing and opening to mask
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7,7))
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

# make mask 3 channel
mask = cv2.merge([mask,mask,mask])

# write
cv2.imwrite("./input_mask.jpg", mask)

cv2.destroyAllWindows()
