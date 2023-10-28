import cv2 as cv
import numpy as np

img = cv.imread("Photos\cat.jpg")
cv.imshow("Cat", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("GRay", gray)

# Simple thresholding
# cv.threshold(image, threshold value, maximum value, type)
threshold, thresh = cv.threshold(gray, 225, 255, cv.THRESH_BINARY)
cv.imshow("Simple Threshold", thresh)


threshold, thresh_inv = cv.threshold(gray, 225, 255, cv.THRESH_BINARY_INV)
cv.imshow("Simple Threshold Inverse", thresh_inv)

# Adaptive Thresholding

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                       cv.THRESH_BINARY, 13 , 3)
cv.imshow("Adaptive Thresholding", adaptive_thresh)


cv.waitKey(0)