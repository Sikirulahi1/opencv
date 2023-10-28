import cv2 as cv
import numpy as np

# def rescaleFrame(frame, scale = 0.75):
#     width = int(frame.shape[1] * scale)
#     height = int(frame.shape[0] * scale)
    
#     dimensions = (width, height)
#     return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

img = cv.imread("Photos\group.jpg")
# img = rescaleFrame(img, scale = 0.15)
cv.imshow("Group of five people", img)

# Convert the colored image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# Reading the xml file
haar_cascade = cv.CascadeClassifier('har_face.xml')
# Pass in the image, scale vector, minimum Neighbors
face_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 2)

print(f'The number of faces found = {len(face_rect)}')

# Look through the image supposedly detected face to draw bounding boxes
for (x, y, w, h) in face_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), thickness=2)
    
cv.imshow('Detected Faces', img)


cv.waitKey(0)