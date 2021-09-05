import cv2
import numpy as np
from skimage.io import imread


image1 = imread('test_image.jpg')
image2 = imread('rainbow.jpeg')
image3 = imread('kunal.jpg')
image4 = imread('akash.png')
# cv2.imshow('result', image)
# cv2.waitKey(0)

# lane_image = np.cpoy(image)
gray = cv2.cvtColor(image4, cv2.COLOR_BGR2GRAY)
cv2.imshow('result', gray)
cv2.waitKey(0)
