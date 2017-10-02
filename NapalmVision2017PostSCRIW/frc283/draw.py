import numpy
import cv2

img_path = "C:\\Users\\FRC_STANDARD_USER\\Desktop\\Python Vision Code\\testimagesmall.png"
img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
rows = img.shape[0]
columns = img.shape[1]
cv2.line(img, (0, 0), (400, 400), (255, 0, 0), 3) #Inputs seem to be image to act on, start coord, end coord, color, and width in px
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
