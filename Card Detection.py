# Title: Cars detection using Python and OpenCV.
# Author: @CodeProgrammer "On Telegram" || @PythonSy "On Instagram".
"""
you need to install OpenCV by using this command in the terminal:
pip install opencv-python
and download "cars.xml" from GitHub.
for more codes you can visit our channel on Telegram: @CodeProgrammer.
"""
import cv2

cascade_src = 'cars.xml'
#The path and name of the video file that contains cars.
video_src = 'video.avi'


cap = cv2.VideoCapture(video_src)
car_cascade = cv2.CascadeClassifier(cascade_src)

while True:
    ret, img = cap.read()
    if (type(img) == type(None)):
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    cv2.imshow('CodeProgrammer', img)
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()