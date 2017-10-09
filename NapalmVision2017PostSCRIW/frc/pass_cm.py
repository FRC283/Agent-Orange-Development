import cv2
import numpy
from networktables import NetworkTables

#TEMPORARY
vid_path = "C:\\Users\\FRC_STANDARD_USER\\Desktop\\Python Vision Code\\Python Vision Repository\\NapalmVision2017PostSCRIW\\test_video.mov"
img_path = "C:\\Users\\FRC_STANDARD_USER\\Desktop\\Python Vision Code\\Python Vision Repository\\NapalmVision2017PostSCRIW\\rgb_hsv.png"

#Constants
IP = "10.2.83.2"
GREEN_LOWER = numpy.array([35, 150, 100])
GREEN_UPPER = numpy.array([80, 255, 255])
TABLE_NAME = "cv_data"

#Main Code 
camera = cv2.VideoCapture(0) #Stores the camera as a video source
print("Camera Opened: " + str(camera.isOpened()))
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
            c0x = c0m['m10']/c0m['m00'] #Center of mass of contour 0 in the x
            c0y = c0m['m01']/c0m['m00'] #Center of mass of contour 0 in the y
            c1x = c1m['m10']/c1m['m00'] #Center of mass of contour 1 in the x
            c1y = c1m['m01']/c1m['m00'] #Center of mass of contour 1 in the y
            cmx = (c0x + c1x)/2 #The image center of mass in x is the average
            cmy = (c0y + c1y)/2 #The image center of mass in y is the average
            height, width, channels = img.shape #Fetch the image properties
            dx = (cmx) - (width - 1) #Calculate the difference in the x between the center of mass and center of image
            dy = (cmy) - (height - 1) #Calculate the difference in the y between the center of mass and the center of image
            table.putNumber("dx", dx) #Our final product is that vector
            table.putNumber("dy", dy)
            print("dx: " + str(dx))
            print("dy: " + str(dy))
            print("---")
            cv2.circle(img, (int(cmx), int(cmy)), 14, (0, 255, 0), 4)
        else:
            print("Cannot find at least 2 contours...")
        cv2.drawContours(img, contours, -1, (0, 0, 255), 3)
        cv2.imshow("incoming image", img)
        cv2.waitKey(0)
    else:
        print("Can't read camera image...")
camera.release #Frees the camera from the program
