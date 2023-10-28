import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpg')

cv.imshow("Cat", img)
blank = np.zeros(img.shape[:2], dtype = 'uint8')
cv.imshow('Blank Image', blank)


rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (img.shape[1]//2 + 45, img.shape[0]//2), 100, 255, -1)
wierd_shape = cv.bitwise_and(rectangle, circle)
cv.imshow("Wierd shape", wierd_shape)

# cv.imshow("Mask", mask)

masked = cv.bitwise_and(img, img, mask = wierd_shape)
cv.imshow("Wierd Shaped Masked Image", masked)


cv.waitKey(0)