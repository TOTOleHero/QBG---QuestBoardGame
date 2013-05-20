from room import RoomConnectorException
from log4py import Logger
import copy
from tile import Tile
from grid import Grid
from connector import Connector

from room import PositionnedRoom

class TileException(Exception):
    pass   

class TableTop(Grid):
    
    def __init__(self):
        self.log = Logger().get_instance(self.__class__.__name__)
        super(TableTop,self).__init__()
        self.rooms = []
        self.lastRooms = []
        self.sizeY = 0
        self.sizeX = 2
        self.initialConnector = Connector(None)
        self.initialConnector.position1X = 0 
        self.initialConnector.position1Y = -1
        self.initialConnector.position2X = 1
        self.initialConnector.position2Y = -1
        self.initialConnector.direction = 'south'
        self.initialConnector.roomDealer = None
        
        
    
    def addRoom(self,connector,roomDealer):
        if roomDealer == None:
            return False
        
        room = roomDealer.getAndRemoveRoom()
        
        if room == None:
            return False
        
        self.log.debug('Add room '+room.name)
        #convert to PostionnedRoom
        room = PositionnedRoom(room)
        self.log.debug('nb tiles '+str(len(room.tiles)))
        self.connectNewRoom(connector,room)
        if room.subType == 'objective-room':
            return False
        return True
    
    def connectNewRoom(self,connector,room):
        
        #=======================================================================
        # #has last room
        # if len(self.lastRooms) == 0:
        #    self.log.debug(room.name + ' is the first room ')
        #    
        # else:
        #    lastRoom = self.lastRooms[-1]
        #    self.log.debug('connect new '+room.name )
        #    if not lastRoom.hasFreeConnector():
        #        raise RoomConnectorException('old room has no free connector')
        #    self.log.debug(' to last '+lastRoom.name)
        #    if not room.hasFreeConnector():
        #        raise RoomConnectorException('new room has no free connector')
        #    self.log.debug('check last connector '+lastRoom.name)
        #    if len(lastRoom.getFreeConnectors()) > 1:
        #        self.log.debug('more than one free connector to connect')
        #        connectTo = lastRoom.getOneFreeConnector()
        #    else:
        #        connectTo = lastRoom.getOneFreeConnector()
        # 
        # if not room.rotateForCompatibleConnector(connectTo):
        #    raise RoomConnectorException('No connector available')
        # 
        # 
        #=======================================================================
        
        #self.lastRooms.append(room)
        self.resizeTableTopAndAddTiles(connector,room)
        
        for connector in room.getFreeConnectors():
            self.log.debug('Add room '+str(connector))
        
            self.addRoom(connector, connector.roomDealer)
        
        
               


        
    def resizeTableTopAndAddTiles(self,connectTo,room):
        self.log.debug('Direction '+connectTo.direction+', resize, old size '+str(self.sizeX)+'x'+str(self.sizeY)+' with '+str(len(self.tiles))+' tiles')
        self.log.debug('A -- room have '+str(len(room.tiles))+' tiles')
        self.log.debug('connectTo:'+str(connectTo))
       
        self.log.debug('room:'+str(room))
       
        actualX = connectTo.position1X
        actualY = connectTo.position1Y
        
        self.log.debug('actualX:'+str(actualX))
        self.log.debug('actualY:'+str(actualY))   
              
        compatibleConnector = room.getCompatibleConnector(connectTo)
        self.log.debug('connect to compatible:'+str(compatibleConnector))
        compatibleConnectorX = compatibleConnector.position1X
        compatibleConnectorY = compatibleConnector.position1Y
        
        translateX = actualX -  compatibleConnectorX
        translateY = actualY -  compatibleConnectorY
        
        self.log.debug('translateX:'+str(translateX))
        self.log.debug('translateY:'+str(translateY))   
              
        
        if connectTo.direction == 'south':
            translateY = translateY + 1   
        elif connectTo.direction == 'north':
            translateY = translateY - 1   
        elif connectTo.direction == 'west':
            translateX = translateX - 1   
        elif connectTo.direction == 'east':
            translateX = translateX + 1   
         
        
        self.log.debug('translateX after adapt :'+str(translateX))
        self.log.debug('translateY after adapt :'+str(translateY))
              
        room.translate(translateX,translateY)       
        
        self.log.debug('translate room:'+str(room))
        
        self.log.debug('B -- room have '+str(len(room.tiles))+' tiles')
        
        expandXeast = 0
        expandXwest = 0
        expandYnorth = 0
        expandYsouth = 0 
        
        self.log.debug('startX:'+str(room.startX))
        self.log.debug('startY:'+str(room.startY))
        self.log.debug('sizeX:'+str(room.sizeX))
        self.log.debug('sizeY:'+str(room.sizeY))
        
        self.log.debug('maxX:'+str(room.getMaxX()))
        self.log.debug('maxY:'+str(room.getMaxY()))
        self.log.debug('minX:'+str(room.getMinX()))
        self.log.debug('minY:'+str(room.getMinY()))
        
        if room.getMaxX() > self.sizeX - 1:
            expandXeast =  room.getMaxX() - ( self.sizeX -1 )
        if room.getMaxY() > self.sizeY - 1:
            expandYsouth =  room.getMaxY() - ( self.sizeY -1)
        if room.getMinX() < 0:
            expandXwest =  abs(room.getMinX())
        if room.getMinY() < 0:
            expandYnorth =  abs(room.getMinY())
        
        self.log.debug('expandXeast:'+str(expandXeast))
        self.log.debug('expandXwest:'+str(expandXwest))
        self.log.debug('expandYnorth:'+str(expandYnorth))
        self.log.debug('expandYsouth:'+str(expandYsouth))
        
        self.log.debug('old size:'+str(self.sizeX)+','+str(self.sizeY))
        
        oldSizeX = self.sizeX
        oldSizeY = self.sizeY
        
        self.sizeX = self.sizeX + expandXeast + expandXwest
        self.sizeY = self.sizeY + expandYnorth + expandYsouth


        self.log.debug('new size:'+str(self.sizeX)+','+str(self.sizeY))
        
        oldTiles = copy.deepcopy(self.tiles)
        
        self.resetGrid()   
        
        for roomLoop in self.lastRooms:
            roomLoop.translate(expandXwest,0)
        
        
        self.log.debug('transfert : start')
        #copy old tiles in new tabletop
        for y in range(0,oldSizeY):
            for x in range(0,oldSizeX):
                oldTileIndex = x + (y * oldSizeX)
                #self.log.debug('transfert :'+str(x+abs(expandXwest))+','+str(y))
                self.setTile(oldTiles[oldTileIndex], x+abs(expandXwest), y)
        self.log.debug('transfert : end')
         
        #for lastRoom in self.lastRooms:
        #    lastRoom.translate(expandXwest,expandYnorth)
                
        room.translate(expandXwest,expandYnorth)
        
        self.log.debug('translate room:'+str(room))
        
        self.log.debug('maxX:'+str(room.getMaxX()))
        self.log.debug('maxY:'+str(room.getMaxY()))
        self.log.debug('minX:'+str(room.getMinX()))
        self.log.debug('minY:'+str(room.getMinY()))
        
        self.log.debug('C -- room have '+str(len(room.tiles))+' tiles')
        count = 1

        for y in range(room.getMinY(),room.getMaxY()+1):
            for x in range(room.getMinX(),room.getMaxX()+1):
                #self.log.debug('['+str(count)+'] Transfer tiles '+str(x)+' '+str(y)+' in '+str(len(self.tiles)))
                targetTile = self.getTile(x, y)
                
                if targetTile == None or targetTile.hasFunction('B'):
                    self.setTile(room.getTile(x,y), x, y)
                else:
                    raise TileException('Tile conflict @ '+str(x)+'/'+str(y))
                count = count + 1
                
        self.lastRooms.append(room)
        
                
        
        
        
        self.log.debug('New size '+str(self.sizeX)+'x'+str(self.sizeY)+' with '+str(len(self.tiles))+' tiles')
        room.lockCompatibleConnector(connectTo.direction,connectTo.roomDealer)         
        
     