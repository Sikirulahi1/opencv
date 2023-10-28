import cv2 as cv
import numpy as np

img = cv.imread("Photos\group.jpg")

cv.imshow("Cats", img)

def rescaleImage(frame, scale= 0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

resized_image = rescaleImage(img)
cv.imshow("Resized Image", resized_image)

cv.waitKey(0)