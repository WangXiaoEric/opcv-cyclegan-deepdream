import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('resources/image_blend2.jpg')
# img = cv.medianBlur(img,5)

blur = cv.GaussianBlur(img,(35,35),0)


cv.imwrite("res/smooth_res.jpg", blur)
