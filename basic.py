import cv2 as cv

img = cv.imread('Photos\group.jpg')
cv.imshow("Group", img)

# Converting an image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# How to blur an image: Blur
# blur = cv.GaussianBlur(image, column size, cv.BORDER_DEFAULT)
# The column size has to be a 2 by 2 tuple and it has to be an odd number
# To increase the blur in the image, we can essentially increate the kernel size
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

# Edge Cascade
# cv.Canny(image, threshold value 1, threshold value 2)
# We can reduce the edges by passing in the blur
# The higher the blur intensity, the lesser the edges it shows
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilating an image
# cv.dilate(image, kernel, iterations)
dilated = cv.dilate(canny, (7, 7), iterations = 3)
cv.imshow("Dilated", dilated)

# Eroding
# cv.erode(image, kernel, iterations)
eroded = cv.erode(dilated, (3, 3), iterations = 3)
cv.imshow('Erode', eroded)

# Resize
# cv.resize(image, destination seize)
resized = cv.resize(img, (500, 500), interpolation = cv.INTER_AREA)
cv.imshow("Resize" ,resized)

# Cropping
# We cropped the image using slicing
cropped = img[50:200, 200:400]
cv.imshow("Crop", cropped)

cv.waitKey(0)