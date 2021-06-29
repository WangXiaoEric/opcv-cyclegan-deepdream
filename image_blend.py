import numpy as np
import cv2 as cv

# img1 = cv.imread('resources/1.png')
# img2 = cv.imread('resources/2.png')
img1 = cv.imread('resources/image_blend1.jpg')
img2 = cv.imread('resources/image_blend2.jpg')
dst = cv.addWeighted(img1,0.7,img2,0.3,0)


# cv.imshow('dst',dst)
cv.imwrite("res/image_blend_test.jpg", dst)
cv.waitKey(0)
cv.destroyAllWindows()