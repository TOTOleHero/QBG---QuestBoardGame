from floor import FloorConnectorException
from log4py import Logger
import copy
from tile import Tile

class TableTop(object):
    
    def __init__(self):
        self.log = Logger().get_instance(self.__class__.__name__)
        self.globalTiles = []
        self.globalWidth = 0
        self.globalHeight = 0
        self.floors = []
        self.lastFloors = []
    
    def addFloor(self,floor):
        self.log.debug('Add floor '+floor.name)
        self.floors.append(floor)
        self.connectNewFloor(floor)
        
        
        
    def resizeTableTopAndAddTiles(self,floor,connectTo):
        self.log.debug('Direction '+connectTo+', resize, old size '+str(self.globalWidth)+'x'+str(self.globalHeight)+' with '+str(len(self.globalTiles))+' tiles')
        oldTiles = copy.deepcopy(self.globalTiles)
        oldWidth = self.globalWidth
        oldHeight = self.globalHeight
        
        self.globalTiles = []
        
        extendSide = 0
        if connectTo == 'north':
            self.globalHeight += floor.tilesHeight
            if self.globalWidth < floor.tilesWidth:
                self.log.debug('('+str(floor.tilesWidth)+' - '+str(self.globalWidth)+') / 2 = ' +str(((floor.tilesWidth - self.globalWidth) / 2)))
        
                extendSide = (floor.tilesWidth - self.globalWidth) / 2
                #add two time extend side in west and east
                self.globalWidth += extendSide
                self.globalWidth += extendSide
            self.log.debug('Add new tiles')
            for tile in floor.tiles:
                self.globalTiles.append(tile)
            self.log.debug('Add old tiles')
            
            appendNewTile = 0          
            for tile in oldTiles:
                if appendNewTile == 0 and oldWidth < self.globalWidth:
                    for i in range(0,extendSide):
                        blankTile = Tile()
                        blankTile.addFunction(floor.tileFunctionLoader.getTileFunctionFromCode('B'))
                        self.globalTiles.append(blankTile)    
                
                self.globalTiles.append(tile)
                appendNewTile += 1
                
                if appendNewTile == oldWidth and oldWidth < self.globalWidth:
                    for i in range(0,extendSide):
                        blankTile = Tile()
                        blankTile.addFunction(floor.tileFunctionLoader.getTileFunctionFromCode('B'))
                        self.globalTiles.append(blankTile)
                    appendNewTile = 0
            
        if connectTo == 'west':
            self.globalWidth += floor.tilesWidth
            appendNewTile = 0          
            for tile in oldTiles:
                self.globalTiles.append(tile)
                appendNewTile += 1
                
                if appendNewTile == oldWidth:
                    for i in range(oldWidth,self.globalWidth):
                        blankTile = Tile()
                        blankTile.addFunction(floor.tileFunctionLoader.getTileFunctionFromCode('B'))
                        self.globalTiles.append(blankTile)
                    appendNewTile = 0
            
            
        self.log.debug('Resize, new size '+str(self.globalWidth)+'x'+str(self.globalHeight)+' with '+str(len(self.globalTiles))+' tiles')
              
    def connectNewFloor(self,floor):
        
        #has last floor
        if len(self.lastFloors) == 0:
            self.log.debug(floor.name + ' is the first floor ')
            connectTo = 'north'
        else:
            lastFloor = self.lastFloors[-1]
            self.log.debug('connect new '+floor.name )
            if not lastFloor.hasFreeConnector():
                raise FloorConnectorException('old floor has no free connector')
            self.log.debug(' to last '+lastFloor.name)
            if not floor.hasFreeConnector():
                raise FloorConnectorException('new floor has no free connector')
            self.log.debug('check last connector '+lastFloor.name)
            if len(lastFloor.getFreeConnectors()) > 1:
                self.log.debug('more than one free connector to connect')
                connectTo = lastFloor.getOneFreeConnector()
            else:
                connectTo = lastFloor.getOneFreeConnector()
        
        if not floor.rotateForCompatibleConnector(connectTo):
            raise FloorConnectorException('No connector available')
        floor.lockCompatibleConnector(connectTo)
        self.lastFloors.append(floor)
        self.resizeTableTopAndAddTiles(floor,connectTo)
        