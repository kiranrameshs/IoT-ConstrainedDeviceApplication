# import the necessary packages
from imutils.video import VideoStream
import argparse
import datetime
import imutils
import time
import cv2
import time


class MotionDetection_SensorData():
    
    def __init__(self):
        print("Motion Detection Init Complete");
        
    def detect_motion(self, args):
        vs = cv2.VideoCapture(args)
        firstFrame = None
        while True:
                frame = vs.read()
                frame = frame[1]
                text = "Unoccupied"
                if frame is None:
                        break
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                gray = cv2.GaussianBlur(gray, (21, 21), 0)
                if firstFrame is None:
                        firstFrame = gray
                        continue
                frameDelta = cv2.absdiff(firstFrame, gray)
                thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
                thresh = cv2.dilate(thresh, None, iterations=2)
                cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)
                cnts = imutils.grab_contours(cnts)
                for c in cnts:
                        if cv2.contourArea(c) < args["min_area"]:
                                continue
                        (x, y, w, h) = cv2.boundingRect(c)
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                        text = "Occupied"
                        print("Status changed")
                        return 1;
        return 0;