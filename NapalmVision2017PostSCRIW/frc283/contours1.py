import cv2
import numpy

vid_path = "C:\\Users\\FRC_STANDARD_USER\\Desktop\\Python Vision Code\\Python Vision Repository\\NapalmVision2017PostSCRIW\\test_video.mov"
vid_path2 = "C:\\Users\Benjamin\\Desktop\\Python\\Python Vision\\Python Vision Repository\\283-Vision\\NapalmVision2017PostSCRIW\\test_video.mov"
cap = cv2.VideoCapture(vid_path2)
GREEN_LOWER = numpy.array([50, 140, 50])
GREEN_UPPER = numpy.array([140, 255, 255])
while True :
    good, img = cap.read()
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(img_hsv, GREEN_LOWER, GREEN_UPPER)
    dumby = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #Draw the two largest contours
    areas = []
    reverse = {}
    index = 0
    for i in dumby[1]:
        areas += [cv2.contourArea(i)]
        reverse.update({cv2.contourArea(i): index})
        index += 1
    areas = sorted(areas, key=float, reverse=True)
    img = cv2.drawContours(img, dumby[1], reverse[areas[0]], (0, 0, 255), 3) 
    img = cv2.drawContours(img, dumby[1], reverse[areas[1]], (0, 0, 255), 3) 
    cv2.imshow("the image", img)
    cv2.waitKey(0)  
cv2.destroyAllWindows()