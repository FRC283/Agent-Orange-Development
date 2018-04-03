import cv2
import numpy

palette_path = "C:\\Users\\FRC_STANDARD_USER\\Desktop\\Python Vision Code\\Python Vision Repository\\NapalmVision2017PostSCRIW\\rgb_hsv.png"
photo_path = "C:\\Users\\FRC_STANDARD_USER\Desktop\\Python Vision Code\\Python Vision Repository\\NapalmVision2017PostSCRIW\\testimagesmall.png"
bright_path = "C:\\Users\\FRC_STANDARD_USER\\Desktop\\Python Vision Code\\Python Vision Repository\\NapalmVision2017PostSCRIW\\bright_test.png"
sat_path = "C:\\Users\\FRC_STANDARD_USER\\Desktop\\Python Vision Code\\Python Vision Repository\\NapalmVision2017PostSCRIW\\sat_test.png"
bd_path = "C:\\Users\\FRC_STANDARD_USER\\Desktop\\Python Vision Code\\Python Vision Repository\\NapalmVision2017PostSCRIW\\bd_test.png"
bb_path = "C:\\Users\\FRC_STANDARD_USER\\Desktop\\Python Vision Code\\Python Vision Repository\\NapalmVision2017PostSCRIW\\bb_test.png"
sd_path = "C:\\Users\\FRC_STANDARD_USER\\Desktop\\Python Vision Code\\Python Vision Repository\\NapalmVision2017PostSCRIW\\scoobydooby.png"


#GREEN_LOWER = numpy.array([70, 170, 80])
#GREEN_UPPER = numpy.array([140, 255, 255])

img = cv2.imread(sd_path)
img_copy = img.copy()
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print("Primary zone values: " + str(img_hsv[80, 210])) 
#print("Paper zone values: " + str(img_hsv[35, 330])) 
GREEN_LOWER = numpy.array([50, 0, 235])
GREEN_UPPER = numpy.array([100, 90, 255])
mask = cv2.inRange(img_hsv, GREEN_LOWER, GREEN_UPPER)
cv2.imshow("mask", mask)
image, cons, hiers = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img_copy, cons, -1, (0, 0, 255), 3) 
cv2.imshow("the image", img_copy)
cv2.waitKey(0)  
cv2.destroyAllWindows()