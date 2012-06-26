from room import RoomConnectorException
from log4py import Logger
import copy
from tile import Tile
from grid import Grid
from connector import Connector

from room import PositionnedRoom

class TableTop(Grid):
    
    def __init__(self):
        self.log = Logger().get_instance(self.__class__.__name__)
        super(TableTop,self).__init__()
        self.rooms = []
        self.lastRooms = []
        self.sizeY = 0
        self.sizeX = 2
        
        
    
    def addRoom(self,room):
        self.log.debug('Add room '+room.name)
        self.connectNewRoom(room)
        
        
        
    def resizeTableTopAndAddTiles(self,room,connectTo):
        self.log.debug('Direction '+connectTo.direction+', resize, old size '+str(self.sizeX)+'x'+str(self.sizeY)+' with '+str(len(self.tiles))+' tiles')
        
        oldTiles = copy.deepcopy(self.tiles)
        self.tiles = []
        
        oldWidth = self.sizeX
        oldHeight = self.sizeY
               
        extendSide = 0
        
        directionTo = connectTo.direction
        
        compatibleConnector = room.getCompatibleConnector(connectTo)
        
        
        
        self.log.debug('connector '+ str(compatibleConnector) );
        
        
        if directionTo == 'south' or directionTo == 'north':
            beforeCompatible =  compatibleConnector.position1X
            afterCompatible = (room.sizeX - 1) - compatibleConnector.position2X
        
        if directionTo == 'east' or directionTo == 'west':
            beforeCompatible =  compatibleConnector.position1Y
            afterCompatible = (room.sizeY - 1) - compatibleConnector.position2Y
        
        if directionTo == 'south':
            self.sizeY = self.sizeY + room.sizeY
            if self.sizeX < room.sizeX:
                self.sizeX = self.sizeX + beforeCompatible + afterCompatible
            
        self.resetGrid()   
        
        
        
        
        self.log.debug('before '+ str(beforeCompatible) + ' after ' + str(afterCompatible));
        
        
                
        
        
        
        self.log.debug('Resize, new size '+str(self.sizeX)+'x'+str(self.sizeY)+' with '+str(len(self.tiles))+' tiles')
        room.lockCompatibleConnector(connectTo.direction)      

    
    def connectNewRoom(self,room):
        
        #has last room
        if len(self.lastRooms) == 0:
            self.log.debug(room.name + ' is the first room ')
            connectTo = Connector(None)
            connectTo.position1X = 0 
            connectTo.position1Y = 0
            connectTo.position2X = 1
            connectTo.position2Y = 0
            connectTo.direction = 'south'
        else:
            lastRoom = self.lastRooms[-1]
            self.log.debug('connect new '+room.name )
            if not lastRoom.hasFreeConnector():
                raise RoomConnectorException('old room has no free connector')
            self.log.debug(' to last '+lastRoom.name)
            if not room.hasFreeConnector():
                raise RoomConnectorException('new room has no free connector')
            self.log.debug('check last connector '+lastRoom.name)
            if len(lastRoom.getFreeConnectors()) > 1:
                self.log.debug('more than one free connector to connect')
                connectTo = lastRoom.getOneFreeConnector()
            else:
                connectTo = lastRoom.getOneFreeConnector()
        
        if not room.rotateForCompatibleConnector(connectTo):
            raise RoomConnectorException('No connector available')
        
        self.lastRooms.append(room)
        self.resizeTableTopAndAddTiles(room,connectTo)
        
        
        
        