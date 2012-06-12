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
        self.globalWidth = floor.tilesWidth
        self.globalHeight = floor.tilesHeight 
        for tile in floor.tiles:
            self.globalTiles.append(tile)
        
              
    def connectNewFloor(self,floor):
        #has last floor
        if len(self.lastFloors) == 0:
            floor.lockConnector('north')
            self.resizeTableTop(floor)
        elif len(self.lastFloors) == 1:
            lastFloor = self.lastFloors[0]
            if not lastFloor.hasFreeConnector():
                raise FloorConnectorException('old floor has no free connector')
            if not floor.hasFreeConnector():
                raise FloorConnectorException('new floor has no free connector')
            if len(lastFloor.getFreeConnectors) > 1:
                pass
            else:
                floor.rotateAndConnectToConnector(lastFloor.getOneFreeConnector())
            
            
            pass
        else:
            pass
        
        
        
        