import cv2
import numpy

path = "C:\\Users\\FRC_STANDARD_USER\Desktop\\Python Vision Code\\Python Vision Repository\\NapalmVision2017PostSCRIW\\testimagesmall.png"
path2 = "C:\\Users\Benjamin\\Desktop\\Python\\Python Vision\\Python Vision Repository\\283-Vision\\NapalmVision2017PostSCRIW\\testimagesmall.png"
img = cv2.imread(path2)
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
GREEN_LOWER = numpy.array([60, 160, 120])
GREEN_UPPER = numpy.array([140, 255, 255])
mask = cv2.inRange(img, GREEN_LOWER, GREEN_UPPER)
cv2.imshow("mask", mask)
cv2.waitKey(0)
cv2.destroyAllWindows()