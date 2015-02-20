import cv2

winName = "Webcam"
cv2.namedWindow(winName, cv2.CV_WINDOW_AUTOSIZE)

cam = cv2.VideoCapture(0)
s, img = cam.read()
key = cv2.waitKey(10)

while key!=27:
  cv2.imshow( winName,img )

  s, img = cam.read()

  key = cv2.waitKey(10)
  
cv2.destroyWindow(winName)