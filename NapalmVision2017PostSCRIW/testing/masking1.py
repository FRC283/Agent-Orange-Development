import cv2

path = "C:\\Users\\FRC_STANDARD_USER\Desktop\\Python Vision Code\\Python Vision Repository\\NapalmVision2017PostSCRIW\\testimagesmall.png"
path2 = "C:\\Users\Benjamin\\Desktop\\Python\\Python Vision\\Python Vision Repository\\283-Vision\\NapalmVision2017PostSCRIW\\testimagesmall.png"
img = cv2.imread(path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_h = img[:,:,0] #Image but ONLY hue values
img_h_copy = img_h
#Green is between 60 and 160
good, img_h = cv2.threshold(img_h, 60, 255, cv2.THRESH_BINARY) #Pixels above 82 become white
good2, img_h2 = cv2.threshold(img[:,:,0], 120, 255, cv2.THRESH_BINARY) #Pixels above 2nd number become white
img_f = cv2.bitwise_xor(img_h, img_h2) 
cv2.imshow("h", img_h)
cv2.imshow("h2", img_h2)
cv2.imshow("combined", img_f)
cv2.waitKey(0)
cv2.destroyAllWindows()