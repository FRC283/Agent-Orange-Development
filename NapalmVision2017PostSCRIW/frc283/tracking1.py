import cv2
import numpy

vid_path = "C:\\Users\\FRC_STANDARD_USER\\Desktop\\Python Vision Code\\Python Vision Repository\\NapalmVision2017PostSCRIW\\test_video.mov"
vid_path2 = "C:\\Users\Benjamin\\Desktop\\Python\\Python Vision\\Python Vision Repository\\283-Vision\\NapalmVision2017PostSCRIW\\test_video.mov"
cap = cv2.VideoCapture(vid_path2)
print(cap.isOpened())
GREEN_LOWER = numpy.array([60, 120, 80])
GREEN_UPPER = numpy.array([140, 255, 255])

while True :
    good, img = cap.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(img, GREEN_LOWER, GREEN_UPPER)
    cv2.imshow("mask", mask)
    cv2.waitKey(0)
cv2.destroyAllWindows()