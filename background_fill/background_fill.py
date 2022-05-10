import numpy as np
import cv2 as cv
import copy

img = cv.imread('bg.jpg')
mask = cv.imread('mask_human.jpg', 0)

mask2 = copy.deepcopy(mask)

# mask adjust

# for i in range(mask.shape[0]):
# 	for j in range(mask.shape[1]):
# 		if mask2[i][j] != 0:
# 			mask2[i][j] == 255;

dst = cv.inpaint(img,mask2,3,cv.INPAINT_TELEA)
# cv.imshow('dst',dst)

cv.imwrite('./filled_bg.jpg',dst)

# cv.waitKey(0)
# cv.destroyAllWindows()