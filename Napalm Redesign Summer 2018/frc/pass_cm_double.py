import cv2
import numpy
from networktables import NetworkTables

#TEMPORARY
vid_path = "C:\\Users\\FRC_STANDARD_USER\\Desktop\\Python Vision Code\\Python Vision Repository\\NapalmVision2017PostSCRIW\\test_video.mov"
img_path = "C:\\Users\\FRC_STANDARD_USER\\Desktop\\Python Vision Code\\Python Vision Repository\\NapalmVision2017PostSCRIW\\rgb_hsv.png"
vid2_path = "C:\\Users\\FRC_STANDARD_USER\\Desktop\\Python Vision Code\\Python Vision Repository\\NapalmVision2017PostSCRIW\\palette.mp4"

#Constants
IP = "10.2.83.5"
GREEN_LOWER = numpy.array([50, 0, 200])
GREEN_UPPER = numpy.array([80, 30, 255])
TABLE_NAME = "cv_data"

#Main Code 
camera = cv2.VideoCapture(0) #Stores the camera as a video source
camera2 = cv2.VideoCapture(1) #Stores the other cam as a source
print("Camera Opened: " + str(camera.isOpened()))
print("Camera2 Opened: " + str(camera2.isOpened()))
NetworkTables.setClientMode()
NetworkTables.initialize(server=IP) #Target to retrieve table from
table = NetworkTables.getTable(TABLE_NAME) #Save the cv_data table to a name.
#The cv_data table is where all values will be written to
while True:
    print("=====")
    is_reading, img = camera.read() #is_reading is true if a image is grabbed. img is the captured image
    #img = cv2.imread(img_path); is_reading = True #Comment in if using static image
    table.putBoolean("is_reading", is_reading) #So the robot can detect the bug status of the program
    if is_reading: #Only continue if we're successfully reading the image. (Prevents crashes)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #Converts the image to Hue-Saturation-Lightness color coordinate scheme
        mask = cv2.inRange(hsv, GREEN_LOWER, GREEN_UPPER) #Returns a binary image of regions that are considered "green"
        #A binary image has only two colors, black and white, which are used to signal properties about areas of the image
        #In this case, WHITE regions represent areas that were considered "green"
        blank, contours, other = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #Finds the curves that enclose "green" areas of the binary image
        if (len(contours) > 1):
            #---Contours Sorting
            #Explanation of Sorting: 
                #A typical areas list would be [1500, 900, 1700, 1100]
                #A typical reverse dict would be {1500: 0, 900:1, 1700:2, 1100:3} which as you can see just reverses the indexes
                #A sorted areas list would be [1700, 1500, 1100, 900]
                #So, by doing areas[0] we access the highest area, 1700
                #And by doing reverse[1700], we get 0, the index of the highest area
                #Hence, reverse[areas[0]] gives the ORIGINAL index of the highest area, 2
                #reverse[areas[1]] is the second-highest, etc 
            areas = [] #A list of contour areas
            reverse = {} #A dictionary of contour indexes INDEXED BY contour areas
            index = 0 #The index number of the contour currently being examined
            for i in contours: #For each contour
                area_i = cv2.contourArea(i) #Calculate the area for that contour
                areas += [area_i] #Add that onto the list of areas
                reverse.update({area_i: index}) #Append its area:index pair onto the reverse dict
                index += 1
            areas = sorted(areas, key=float, reverse=True) #Sort the areas list so that the highest areas are in the lowest indices
            #---End of Sorting
            c0m = cv2.moments(contours[reverse[areas[0]]]) #Moments (number-data) about the highest-area contour
            c1m = cv2.moments(contours[reverse[areas[1]]]) #Moments (number-data) about the second-highest-area contour
            if c0m['m00'] != 0 and c1m['m00'] != 0: #Avoid division by 0
                c0x = c0m['m10']/c0m['m00'] #Center of mass of contour 0 in the x
                c0y = c0m['m01']/c0m['m00'] #Center of mass of contour 0 in the y
                c1x = c1m['m10']/c1m['m00'] #Center of mass of contour 1 in the x
                c1y = c1m['m01']/c1m['m00'] #Center of mass of contour 1 in the y
                cmx = (c0x + c1x)/2 #The image center of mass in x is the average
                cmy = (c0y + c1y)/2 #The image center of mass in y is the average
                height, width, channels = img.shape #Fetch the image properties
                dx = (cmx) - (width - 1)/2 #Calculate the difference in the x between the center of mass and center of image
                dy = (cmy) - (height - 1)/2 #Calculate the difference in the y between the center of mass and the center of image
                table.putNumber("dx", dx) #Our final product is that vector
                table.putNumber("dy", dy)
                print("dx: " + str(dx))
                print("dy: " + str(dy))
                cv2.circle(img, (int(cmx), int(cmy)), 14, (0, 255, 0), 4)
            else:
                print("A contour's m00 = 0!")
                print("Updating dy = 0 and dx = 0")
                table.putNumber("dx", 0)
                table.putNumber("dy", 0)
        else:
            print("Cannot find at least 2 contours...")
        cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
        cv2.imshow("incoming image", img)
        cv2.waitKey(0)
    else:
        print("Can't read camera image...")
    
    is_reading2, img2 = camera2.read() #is_reading is true if a image is grabbed. img is the captured image
    #img = cv2.imread(img_path); is_reading = True #Comment in if using static image
    table.putBoolean("is_reading2", is_reading2) #So the robot can detect the bug status of the program
    if is_reading: #Only continue if we're successfully reading the image. (Prevents crashes)
        hsv2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV) #Converts the image to Hue-Saturation-Lightness color coordinate scheme
        mask2 = cv2.inRange(hsv2, GREEN_LOWER, GREEN_UPPER) #Returns a binary image of regions that are considered "green"
        #A binary image has only two colors, black and white, which are used to signal properties about areas of the image
        #In this case, WHITE regions represent areas that were considered "green"
        blank2, contours2, other2 = cv2.findContours(mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #Finds the curves that enclose "green" areas of the binary image
        if (len(contours2) > 1):
            #---Contours Sorting
            #Explanation of Sorting: 
                #A typical areas list would be [1500, 900, 1700, 1100]
                #A typical reverse dict would be {1500: 0, 900:1, 1700:2, 1100:3} which as you can see just reverses the indexes
                #A sorted areas list would be [1700, 1500, 1100, 900]
                #So, by doing areas[0] we access the highest area, 1700
                #And by doing reverse[1700], we get 0, the index of the highest area
                #Hence, reverse[areas[0]] gives the ORIGINAL index of the highest area, 2
                #reverse[areas[1]] is the second-highest, etc 
            areas2 = [] #A list of contour areas
            reverse2 = {} #A dictionary of contour indexes INDEXED BY contour areas
            index2 = 0 #The index number of the contour currently being examined
            for i2 in contours2: #For each contour
                area_i2 = cv2.contourArea(i2) #Calculate the area for that contour
                areas2 += [area_i2] #Add that onto the list of areas
                reverse2.update({area_i2: index2}) #Append its area:index pair onto the reverse dict
                index2 += 1
            areas2 = sorted(areas2, key=float, reverse=True) #Sort the areas list so that the highest areas are in the lowest indices
            #---End of Sorting
            c0m2 = cv2.moments(contours2[reverse2[areas2[0]]]) #Moments (number-data) about the highest-area contour
            c1m2 = cv2.moments(contours2[reverse2[areas2[1]]]) #Moments (number-data) about the second-highest-area contour
            if c0m2['m00'] != 0 and c1m2['m00'] != 0: #Avoid division by 0
                c0x2 = c0m2['m10']/c0m2['m00'] #Center of mass of contour 0 in the x
                c0y2 = c0m2['m01']/c0m2['m00'] #Center of mass of contour 0 in the y
                c1x2 = c1m2['m10']/c1m2['m00'] #Center of mass of contour 1 in the x
                c1y2 = c1m2['m01']/c1m2['m00'] #Center of mass of contour 1 in the y
                cmx2 = (c0x2 + c1x2)/2 #The image center of mass in x is the average
                cmy2 = (c0y2 + c1y2)/2 #The image center of mass in y is the average
                height2, width2, channels2 = img2.shape #Fetch the image properties
                dx2 = (cmx2) - (width2 - 1)/2 #Calculate the difference in the x between the center of mass and center of image
                dy2 = (cmy2) - (height2 - 1)/2 #Calculate the difference in the y between the center of mass and the center of image
                table.putNumber("dx2", dx2) #Our final product is that vector
                table.putNumber("dy2", dy2)
                print("dx2: " + str(dx2))
                print("dy2: " + str(dy2))
                cv2.circle(img2, (int(cmx2), int(cmy2)), 14, (0, 255, 0), 4)
            else:
                print("2: A contour's m00 = 0!")
                print("2: Updating dy = 0 and dx = 0")
                table.putNumber("dx2", 0)
                table.putNumber("dy2", 0)
        else:
            print("2: Cannot find at least 2 contours...")
        cv2.drawContours(img2, contours2, -1, (0, 0, 255), 3)
        cv2.imshow("incoming image2", img2)
        cv2.waitKey(0)
    else:
        print("Can't read camera2 image...")
camera.release #Frees the camera from the program
