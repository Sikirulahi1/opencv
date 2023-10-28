import cv2 as cv
import numpy as np

img = cv.imread("Photos\cat.jpg")
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Cat", img)

modes = (cv.THRESH_BINARY,
cv.THRESH_BINARY_INV,
cv.THRESH_TRUNC,
cv.THRESH_TOZERO,
cv.THRESH_TOZERO_INV)

def threshold(x):
    rec, img1 = cv.threshold(img, x, 255, cv.THRESH_BINARY)
    rec, img2 = cv.threshold(img, x, 255, cv.THRESH_BINARY_INV)
    rec, img3 = cv.threshold(img, x, 255, cv.THRESH_TRUNC)
    rec, img4 = cv.threshold(img, x, 255, cv.THRESH_TOZERO)
    rec, img5 = cv.threshold(img, x, 255, cv.THRESH_TOZERO_INV)
    ret, img6 = cv.threshold(img, x, 255, cv.THRESH_TOZERO)
    ret, img7 = cv.threshold(img, x, 255, cv.THRESH_TOZERO_INV)

    
    cv.imshow("Window", np.hstack([img, img1]))
    cv.imshow('Window 2', np.hstack([img2, img3]))
    cv.imshow('Window 3', np.hstack([img4, img5]))
    cv.imshow('window 4', np.hstack([img6, img7]))

threshold(200)

cv.waitKey(0)
cv.destroyAllWindows()