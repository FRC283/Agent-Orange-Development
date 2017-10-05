import cv2
import numpy
from networktables import NetworkTables

#Constants
IP = "10.28.3.2"
GREEN_LOWER = numpy.array([70, 150, 150])
GREEN_UPPER = numpy.array([140, 255, 255])

#Main Code
camera = cv2.VideoCapture(0) #Stores the camera as a video source
NetworkTables.initialize(server=IP) #Target to retrieve table from
table = NetworkTables.getTable("cv_data") #Save the cv_data table to a name.
#The cv_data table is where all values will be written to
while True:
    is_reading, img = camera.read() #is_reading is true if a image is grabbed. img is the captured image
    table.putBoolean("is_reading", is_reading) #So the robot can detect the bug status of the program
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #Converts the image to Hue-Saturation-Lightness color coordinate scheme
    
    
    
    
    break
camera.release #Frees the camera from the program
