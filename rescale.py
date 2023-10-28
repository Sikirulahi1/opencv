import cv2 as cv

img = cv.imread("Photos\cat_large.jpg")
cv.imshow('Cat', img)

# We create the function
def rescaleFrame(frame, scale = 0.75):
    # It works for images, videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

# Resizing an image
resized_image = rescaleFrame(img, scale= 0.2)
cv.imshow("Resized Image", resized_image)


def changeRes(width, height):
    # It only works for live videos
    capture.set(3, width)
    capture.set(4, height)


# Resizing a video
# Reading Videos
capture = cv.VideoCapture("Videos\cars.mp4")

while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)
    
    frame_resized = rescaleFrame(frame, scale = 0.2)
    
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    
    if cv.waitKey(20) & 0xFF== ord("d"):
        break

capture.release()
cv.destroyAllWindows()