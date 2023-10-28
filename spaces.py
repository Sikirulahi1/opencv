import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("Photos\group.jpg")
cv.imshow("People", img)

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale Image", gray)

# BGR to HSV (Hue Saturation Value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

# BGR to l*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)
plt.show()

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV --> BGR', hsv_bgr)

# LAB to BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR', lab_bgr)

# plt.imshow(rgb)
# plt.show()

cv.waitKey(0)