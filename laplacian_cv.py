import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('resources/image_blend2.jpg',0)
laplacian = cv.Laplacian(img,2,ksize=3)

cv.imwrite("res/laplacian_res.jpg", laplacian)

