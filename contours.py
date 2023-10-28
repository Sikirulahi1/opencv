import cv2 as cv
import numpy as np

img = cv.imread("Photos\cat.jpg")
cv.imshow('Cat', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

blank = np.zeros(img.shape, dtype = 'uint8')
cv.imshow('Blank', blank)

# blur
blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

# Getting the edges using the canny edge detector
canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny Edges", canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("Threshold", thresh)


# Contours
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} found')

# We want to draw our contours on that black image to know the number of contours that opencv found
# cv.drawContours(image, contours, contours index, color, thckness)
cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow("Contours Drawn", blank)


cv.waitKey(0)