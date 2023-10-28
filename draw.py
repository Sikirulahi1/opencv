import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow("Blank", blank)

# 1. Paint the image a certain color
# blank[:] = 0, 255, 0
# cv.imshow('Green', blank)

# To color certain portion of the image by basically giving it a number of pixels
# blank[200:300, 300:400] = 0, 0, 255
# cv.imshow('Green', blank)

# 2. To draw  Rectangle
# cv.rectange(image, start position, end position, color, thickness)
cv.rectangle(blank, (0, 0),  (blank.shape[0]//2, blank.shape[1]//2), (0, 255, 0), thickness = -1)
cv.imshow("Blank", blank)

# 3. Draw a circle
# cv.circle(image, center, radius, color, thickness)
cv.circle(blank, (blank.shape[0]//2, blank.shape[1]//2), 40, (0, 0, 255), thickness = -1)
cv.imshow("Circle", blank)

# 4. Draw a line
# cv.line(image, start position, end position, color, thickness)
cv.line(blank, (100, 250), (300, 250), (255, 255, 255), thickness = 3)
cv.imshow("Blank", blank)


# 5. Write text on an image
# cv.putText(image, text, position, font face, font_scale, color, thickness)
cv.putText(blank, 'Hello my name is Sikirulahi!! ', (0, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow("Blank", blank)

cv.waitKey(0)