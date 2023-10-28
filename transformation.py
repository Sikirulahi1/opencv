import cv2 as cv
import numpy as np

img = cv.imread("Photos\cat.jpg")
cv.imshow('Cat', img)


# Translation
# x and y represent the numbers of pixels you want to shift on the x and y axis respectively
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]]) # We created a translation matrix
    dimensions = (img.shape[1], img.shape[0]) # We set the dimensions
    return cv.warpAffine(img, transMat, dimensions) # We group everything together using the warpAffine method

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

# shifting down and right by 100 pixels
translated = translate(img, 100, 100)
cv.imshow("Translated", translated)

# Shifting down and left by 100 pixels
translated = translate(img, -100, 100)
cv.imshow("Translated", translated)



# Rotation
def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2] # We get our height and width
    
    if rotPoint is None:
        rotPoint = (width//2, height//2)
        
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) # We get our rotation matrix
    dimensions = (width, height) # We reset our dimensions
    return cv.warpAffine(img, rotMat, dimensions) # We use cv.warpAffine method to put everything together


# To rotate clockwise : specify a negative for the angle
# To rotate anticlockwise : specify a positive value for the angle
rotated = rotate(img, 45)
cv.imshow("Rotated", rotated)

cw_rotated = rotate(img, -45)
cv.imshow("Clockwise Rotated", cw_rotated)

rotated_rotated = rotate(cw_rotated, -45)
cv.imshow("Rotated Rotated", rotated_rotated)

# Resizing
resized = cv.resize(img, (500, 500), interpolation = cv.INTER_CUBIC)
cv.imshow("Resized", resized)


# flipping
# cv.flip(image, flip code)
# The flip code can be 0, 1 or -1
# 0 means flipping vertically or over the x axis
# 1 means flipping horizontally or over the y axis
# -1 means flipping both vertically and horizontally
v_flip = cv.flip(img, 0) # Verical flip
cv.imshow("Vertical Flip", v_flip)

h_flip = cv.flip(img, 1)
cv.imshow("Horizontal Flip", h_flip)

vh_flip = cv.flip(img, -1)
cv.imshow("Vertically & Horizontal Flip", vh_flip)


# Cropping
cropped = img[200:400, 300:400]
cv.imshow("Cropped", cropped)


cv.waitKey(0)