import numpy
import cv2

img = cv2.imread("C:\\Users\\FRC_STANDARD_USER\\Desktop\\Python Vision Code\\testimagesmall.png", cv2.IMREAD_UNCHANGED)
print(img[0][100]) #BGRA array for pixel indexes 0 and 100
print(img[0, 100]) #Same exact functionality
for i in img[50:60]: #Iterate through rows 50->100
    for h in img[i][50:60]: #Iterate through colmunes 50->100
        img[i][h] = (255, 255, 255, 255); #Set each of those pixels to white
        print("Changing a pixel to white...")
        #print("Changing the color of pixel (" + str(i) + ")(" + str(h) + ")")
cv2.imshow("test image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()