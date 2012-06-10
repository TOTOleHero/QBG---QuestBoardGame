from floor import FloorConnectorException


class TableTop(object):
    
    def __init__(self):
        self.globalTiles = []
        self.globalWidth = 0
        self.globalHeight = 0
        self.floors = []
        self.lastFloors = []
    
    def addFloor(self,floor):
        self.floors.append(floor)
        self.connectNewFloor(floor)
        
        
        
    def resizeTableTop(self,floor):
        self.globalWidth = floor.width
        self.globalHeight = floor.height 
        self.globalTiles = []
              
    def connectNewFloor(self,floor):
        #has last floor
        if len(self.lastFloors) == 0:
            self.resizeTableTop(floor)
        elif len(self.lastFloors) == 1:
            lastFloor = self.lastFloors[0]
            if not lastFloor.hasConnector():
                raise FloorConnectorException()
            #connect to good direction
            pass
        else:
            pass
        
        
        
        