import cv2

vid_path = ""
cap = cv2.VideoCapture(vid_path)
#First, we convert to hue-saturation-lightness colorspace
frame = cap.read();
hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #Converts to hsv color space