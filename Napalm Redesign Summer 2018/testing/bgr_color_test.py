import cv2
import numpy

test_path = "C:\\Users\\FRC_STANDARD_USER\\Desktop\\Python Vision Code\\Python Vision Repository\\NapalmVision2017PostSCRIW\\rgb_hsv.png"
photo_path = "C:\\Users\\FRC_STANDARD_USER\Desktop\\Python Vision Code\\Python Vision Repository\\NapalmVision2017PostSCRIW\\testimagesmall.png"

img = cv2.imread(photo_path)
#img = cv2.imread(test_path)
img_copy = img.copy()
GREEN_LOWER = numpy.array([0, 30, 0]) #BGR COLOR VALUES
GREEN_UPPER = numpy.array([80, 255, 80]) #BGR COLOR VALUES
mask = cv2.inRange(img, GREEN_LOWER, GREEN_UPPER)
cv2.imshow("mask", mask)
image, cons, hiers = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img_copy, cons, -1, (0, 0, 255), 3) 
cv2.imshow("the image", img_copy)
cv2.waitKey(0)  
cv2.destroyAllWindows()