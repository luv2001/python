import cv2
import numpy as np
from skimage.io import imread


# image = imread('test_image.jpg')

# image = imread('rainbow.jpeg')
# image3 = imread('kunal.jpg')
image = imread('akash.png')
# cv2.imshow('result', image)
# cv2.waitKey(0)
# lane_image = np.cpoy(image)


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray, (5, 5), 0)

canny = cv2.Canny(blur, 50, 150)

cv2.imshow('result', canny)
cv2.waitKey(0)
