import cv2 as cv
import numpy as np

img = cv.imread("Photos\cat.jpg")
cv.imshow("Cat", img)
img = cv.resize(img, None, fx = 0.5, fy = 0.5, interpolation = cv.INTER_CUBIC)
M = np.ones(img.shape, dtype =np.uint8) * 40
cv.imshow('M', M)

brighter = cv.add(img, M)
darker = cv.subtract(img, M)

img2 = np.hstack([img, brighter, darker])
cv.imshow("Images", img2)


# How to do histogram stuff
# cv.calcHist([img], channels, mask, bins, ranges)

cv.waitKey(0)
cv.destroyAllWindows()