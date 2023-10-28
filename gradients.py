import cv2 as cv
import numpy as np

img = cv.imread("Photos\group.jpg")
cv.imshow("People", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Laplacian
# cv.Laplacian(image, data depth)
lap = cv.Laplacian(img, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)


# Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)


cv.imshow('Sobelx', sobelx)
cv.imshow('Sobely', sobely)
cv.imshow('Combined Sobel', combined_sobel)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)


cv.waitKey(0)