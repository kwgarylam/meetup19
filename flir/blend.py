#!/usr/bin/python3
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#
# blend.py
# FLIR Camera + Raspberry Pi Camera alpha blending
#
# Author : sosorry
# Date   : 2017/07/31
# Usage  : python blend.py

import cv2
import numpy as np
import time
import imutils

def nothing(x):
    pass

cv2.namedWindow('blend', cv2.WINDOW_NORMAL)
cv2.createTrackbar('alpha', 'blend', 0, 10, nothing)

# FLIR Camera
flr = cv2.VideoCapture(1)

# Raspberry Pi Camera
cam = cv2.VideoCapture(0)

while True:
    alpha = cv2.getTrackbarPos('alpha', 'blend')
    ret, img1 = flr.read()
    ret, img2 = cam.read()

    img1 = imutils.resize(img1, 320)
    img2 = imutils.resize(img2, 320)

    cv2.resizeWindow('blend', 320, 240)
    cam_alpha = float(alpha)/10
    flir_alpha = float(10-alpha)/10
    dst = cv2.addWeighted(img1, cam_alpha, img2, flir_alpha, 0)
    cv2.imshow("blend", dst)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    time.sleep(0.01)

flr.release()
cam.release()
cv2.destroyAllWindows()

