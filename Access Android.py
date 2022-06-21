#Title: Access Android Camera Using OpenCV.
#Author: @CodeProgrammer on Telegram.

#don't forget install OpenCv and numpy.
import urllib.request
import cv2
import numpy as np
import time

#enter Your IP Camera.
URL = "put here your IP Camera"
while True:
    img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
    img = cv2.imdecode(img_arr,-1)
    cv2.imshow('IPWebcam',img)
    
    if cv2.waitKey(1):
        break