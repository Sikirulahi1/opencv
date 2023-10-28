import cv2 as cv
import numpy as np

img = cv.imread("Photos\group.jpg")
cv.imshow('People', img)

# Averaging
average = cv.blur(img, (7, 7))
cv.imshow("Average Blur", average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow("Gaussian Blur", gauss)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow("Medium Blur", median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow("Bilateral", bilateral)


cv.waitKey(0)