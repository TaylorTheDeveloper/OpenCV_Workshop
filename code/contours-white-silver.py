#!/usr/bin/env python
import numpy as np
import cv2
import cv2.cv as cv
from video import create_capture
from common import clock, draw_str

def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

if __name__ == '__main__':
    import sys, getopt

    args, video_src = getopt.getopt(sys.argv[1:], '', ['cascade=', 'nested-cascade='])
    try: video_src = video_src[0]
    except: video_src = 0
    args = dict(args)

    cam = create_capture(video_src, fallback='synth:bg=../cpp/lena.jpg:noise=0.05')

    #Open Cam and load our source details
    ret, img = cam.read()
    src_Height, src_Width, src_Depth = img.shape
    src_Area = src_Width * src_Height

    while True:
        ret, img = cam.read()
        t = clock()

        img = cv2.flip(img,1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)
 

        vis = img.copy()

        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        #Blur
        kernel = np.ones((5,5),np.uint8)
        t = clock()
        vis = cv2.GaussianBlur(hsv,(15,15),30)
        #vis = cv2.erode(vis, kernel, iterations=1)
        vis = cv2.dilate(vis, kernel, iterations=1)
        dt = clock()-1
        print dt
        #Blur 

        #How to define this range for white color #HSV: Hue, Saturation, Value
        sensitivity = 75
        lower_white = np.array([0,0,255-sensitivity]) 
        upper_white = np.array([255,sensitivity,255])
        lower_gray = np.array([0,0,128-sensitivity])
        upper_gray = np.array([255,sensitivity,255])


        # Threshold the HSV image to get only blue colors
        graymask = cv2.inRange(vis, lower_gray, upper_gray)

        whitemask = cv2.inRange(vis, lower_white, upper_white)
        # Bitwise-AND mask and original image
        res_g = cv2.bitwise_and(vis,vis, mask= graymask)

        res_w = cv2.bitwise_and(vis,vis, mask= whitemask)
        kernel1 = np.ones((3,3),np.uint8)
        res_g = cv2.GaussianBlur(res_g,(5,5),30)
        res_w = cv2.GaussianBlur(res_w,(5,5),30)

        #gray contours
        lines_g = cv2.cvtColor(res_g, cv2.COLOR_HSV2BGR)
        lines_g = cv2.cvtColor(lines_g, cv2.COLOR_BGR2GRAY)
        ret_g, thresh_g = cv2.threshold(lines_g,127,255,0)
        contours_g, hierarchy_g = cv2.findContours(thresh_g, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        #White Contours
        lines = cv2.cvtColor(res_w, cv2.COLOR_HSV2BGR)
        lines = cv2.cvtColor(lines, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(lines,127,255,0)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        gray = cv2.drawContours(img, contours_g, -1, (0,0,255), -1)
        white = cv2.drawContours(img, contours, -1, (255,0,0), -1)
   
        #Contours
        #image moments
        if contours:
            for cnt in contours:
                if cv2.contourArea(cnt) > src_Area/15:
                    moments = cv2.moments(cnt)
                    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
                    
                    if len(approx) > 4: #If we have a top left and bottom right for a car shape, greater then four sides, less than 10
                        #Outlines countour
                        cv2.drawContours(img, [cnt], 0, (0,255,0), 3) 
                        x1,y1 = approx[0][0][0], approx[0][0][1]
                        x2,y2 = approx[2][0][0], approx[2][0][1] 
                        cv2.rectangle(img,(x1,y1), (x2,y2),(0,0,255),10)

        cv2.imshow('img',img)


        dt = clock() - t
        
        draw_str(vis, (20, 20), 'time: %.1f ms' % (dt*1000))

        if 0xFF & cv2.waitKey(5) == 27:
            break
    cv2.destroyAllWindows()
