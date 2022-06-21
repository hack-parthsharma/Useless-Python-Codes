# Title: Face detection using Python and OpenCV.
# Author: @CodeProgrammer "On Telegram" || @PythonSy "On Instagram".
"""
you need to install OpenCV by using this command in the terminal:
pip install opencv-python
for more codes you can visit our channel on Telegram: @CodeProgrammer
"""
import cv2

"""
load the cascade file from:
https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
"""
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('3.jpg')
img = cv2.resize(img, (500, 500))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces.
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Draw rectangle around the faces.
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Show the result.
cv2.imshow('by: @CodeProgrammer', img)
cv2.waitKey()
