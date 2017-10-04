import numpy
import cv2

img = cv2.imread("C:\\Users\\FRC_STANDARD_USER\\Desktop\\Python Vision Code\\testimagesmall.png", cv2.IMREAD_UNCHANGED)
print(img.item(10, 10, 2))
#Selecting an ROI (Region of interest)
sub_img = img[10:40, 50:200]
cv2.imshow("sub_img", sub_img)
#Making a region lack blue
img[:,:,0] = 0
cv2.imshow("img no blue", img)

cv2.waitKey(0)
cv2.destroyAllWindows()