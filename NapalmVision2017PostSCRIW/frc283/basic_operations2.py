import numpy
import cv2

img = cv2.imread("C:\\Users\\FRC_STANDARD_USER\\Desktop\\Python Vision Code\\testimagesmall.png", cv2.IMREAD_UNCHANGED)
print(img.item(10, 10, 2))

cv2.waitKey(0)
cv2.destroyAllWindows()