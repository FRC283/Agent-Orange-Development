from networktables import NetworkTables
import logging

logging.basicConfig(level=logging.DEBUG)
NetworkTables.setClientMode()
NetworkTables.setTeam(283)
#NetworkTables.initialize(server="10.2.83.2") #
NetworkTables.setIPAddress("10.2.83.5")
table = NetworkTables.getTable("cv_data")
while True:
    table.putNumber("dx", 44)
    print("testNum: " + str(table.getNumber("testNum", 0)))
    #print("dy: " + str(table.getNumber("dy", 0)))
    print("is conn'd?: " + str(table.isConnected()))
    print("====")