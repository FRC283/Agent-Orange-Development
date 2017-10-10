import cv2
import numpy

path = "C:\\Users\\FRC_STANDARD_USER\Desktop\\Python Vision Code\\Python Vision Repository\\NapalmVision2017PostSCRIW\\testimagesmall.png"
path2 = "C:\\Users\Benjamin\\Desktop\\Python\\Python Vision\\Python Vision Repository\\283-Vision\\NapalmVision2017PostSCRIW\\testimagesmall.png"
img_path = "C:\\Users\\FRC_STANDARD_USER\\Desktop\\Python Vision Code\\Python Vision Repository\\NapalmVision2017PostSCRIW\\rgb_hsv.png"
img2_path = "C:\\Users\\FRC_STANDARD_USER\Desktop\\Python Vision Code\\Python Vision Repository\\NapalmVision2017PostSCRIW\\testimagesmall.png"

img = cv2.imread(img_path)
img_copy = img.copy()
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
GREEN_LOWER = numpy.array([35, 150, 10])
GREEN_UPPER = numpy.array([80, 255, 255])
mask = cv2.inRange(img_hsv, GREEN_LOWER, GREEN_UPPER)
image, cons, hiers = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#Draw the two largest contours
cv2.drawContours(img_copy, cons, -1, (0, 0, 255), 3) 
cv2.imshow("the image", img_copy)
cv2.waitKey(0)  
cv2.destroyAllWindows()