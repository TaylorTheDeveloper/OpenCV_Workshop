#!/usr/bin/env python

import numpy as np
import cv2
import cv2.cv as cv
from video import create_capture

#Detect Cascades patterns with detect multiscale
#Returns rectangle points
def detect(img, cascade):
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30))
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

# Draw Rectangle helper function
def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

#Draw String help function
def draw_str(dst, (x, y), s):
    cv2.putText(dst, s, (x+1, y+1), cv2.FONT_HERSHEY_PLAIN, 1.0, (0, 0, 0), thickness = 2, lineType=cv2.CV_AA)
    cv2.putText(dst, s, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.0, (255, 255, 255), lineType=cv2.CV_AA)

def clock():
    return cv2.getTickCount() / cv2.getTickFrequency()

if __name__ == '__main__':
    import sys, getopt

    args, video_src = getopt.getopt(sys.argv[1:], '',)
    try: video_src = video_src[0]
    except: video_src = 0
    args = dict(args)

    #cascade_fn = "cascades/hogcascade_pedestrians.xml"
    #cascade_fn = "cascades/lbpcascade_face.xml"
    #cascade_fn = "cascades/lbpcascade_seminole.xml"
    #cascade_fn = "cascades/haarcascade_nose.xml"
    #cascade_fn = "cascades/haarcascade_face.xml"
    cascade_fn = "cascades/haarcascade_eye.xml"
    nested_fn  = "cascades/haarcascade_eye.xml"

    cascade = cv2.CascadeClassifier(cascade_fn)
    nested = cv2.CascadeClassifier(nested_fn)

    cam = create_capture(video_src, fallback='img/people.jpg:noise=0.05')

    while True:
    	#Read Image
        ret, img = cam.read()

        t = clock()

        #Convert to Gray and Equalize
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        #Main Classifier
        rects = detect(gray, cascade)
        vis = img.copy()
        draw_rects(vis, rects, (0, 255, 0))

        # Nested Classifiers
        # for x1, y1, x2, y2 in rects:
        #     roi = gray[y1:y2, x1:x2]
        #     vis_roi = vis[y1:y2, x1:x2]
        #     subrects = detect(roi.copy(), nested)
        #     draw_rects(vis_roi, subrects, (255, 0, 0))

        dt = clock() - t

        draw_str(vis, (20, 20), 'time: %.1f ms' % (dt*1000))
        cv2.imshow('facedetect', vis)

        # Use Escape key to quit
        if 0xFF & cv2.waitKey(5) == 27:
            break

    #Terminate Program
    cv2.destroyAllWindows()
