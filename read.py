import cv2 as cv

# Reading images on opencv
# img = cv.imread('Photos/cat_large.jpg')

# cv.imshow("Cat", img)


# Reading a video on opencv
# The parenthesis may contain 0, 1, 2, 3 or the path to the video file
# If you want to use webcam, like ive videos, you use number
# But if you just want to read a video, you use the path to the video file
capture = cv.VideoCapture("Videos\cars.mp4")

while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)
    
    if cv.waitKey(20) & 0xFF== ord("d"):
        break

capture.release()
cv.destroyAllWindows()
        

