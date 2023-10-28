import cv2 as cv
import numpy as np
BLUE = (255, 0, 0)
center = 200, 50
axes = 100, 30
angle = 15
img = img = np.zeros((100, 500, 3), np.uint8)
cv.ellipse(img, center, axes, angle, 0, 360, BLUE, 2)
cv.imshow('RGB', img)

RED = (0, 0, 255)
pts = [(50, 50), (300, 190), (400, 10)]
img = img = np.zeros((200, 500, 3), np.uint8)
cv.polylines(img, np.array([pts]), True, RED, 5)
cv.imshow('window', img)

v = np.fromfunction(lambda i, j : i, (256, 256), dtype = np.uint8)
h = np.fromfunction(lambda i, j : j, (256, 256), dtype = np.uint8)
z = np.zeros((256, 256), dtype = np.uint8)

img = cv.merge([h, v, z])
cv.imshow("Merged colors", img)





cv.waitKey(0)
cv.destroyAllWindows()