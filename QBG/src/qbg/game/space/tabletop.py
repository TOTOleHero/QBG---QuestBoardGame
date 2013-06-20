from qbg.game.space.zone import ZoneConnectorException
from log4py import Logger
import copy
from qbg.game.space.tile import Tile
from qbg.game.space.grid import Grid
from qbg.game.space.connector import Connector

from qbg.game.space.zone import PositionnedZone

class TileException(Exception):
    pass   

class TableTop(Grid):
    
    def __init__(self):
        self.log = Logger().get_instance(self.__class__.__name__)
        super(TableTop,self).__init__()
        self.zones = []
        self.lastZones = []
        self.sizeY = 0
        self.sizeX = 2
        self.initialConnector = Connector(None)
        self.initialConnector.position1X = 0 
        self.initialConnector.position1Y = -1
        self.initialConnector.position2X = 1
        self.initialConnector.position2Y = -1
        self.initialConnector.direction = 'south'
        self.initialConnector.zoneDealer = None
        
        
    
    def addZone(self,connector,zoneDealer):
        if zoneDealer == None:
            return False
        
        zone = zoneDealer.getAndRemoveZone()
        
        if zone == None:
            return False
        
        self.log.debug('Add zone '+zone.name)
        #convert to PostionnedZone
        zone = PositionnedZone(zone)
        self.log.debug('nb tiles '+str(len(zone.tiles)))
        self.connectNewZone(connector,zone)
        if zone.subType == 'objective-zone':
            return False
        return True
    
    def connectNewZone(self,connector,zone):
        
        #=======================================================================
        # #has last zone
        # if len(self.lastZones) == 0:
        #    self.log.debug(zone.name + ' is the first zone ')
        #    
        # else:
        #    lastZone = self.lastZones[-1]
        #    self.log.debug('connect new '+zone.name )
        #    if not lastZone.hasFreeConnector():
        #        raise ZoneConnectorException('old zone has no free connector')
        #    self.log.debug(' to last '+lastZone.name)
        #    if not zone.hasFreeConnector():
        #        raise ZoneConnectorException('new zone has no free connector')
        #    self.log.debug('check last connector '+lastZone.name)
        #    if len(lastZone.getFreeConnectors()) > 1:
        #        self.log.debug('more than one free connector to connect')
        #        connectTo = lastZone.getOneFreeConnector()
        #    else:
        #        connectTo = lastZone.getOneFreeConnector()
        # 
        # if not zone.rotateForCompatibleConnector(connectTo):
        #    raise ZoneConnectorException('No connector available')
        # 
        # 
        #=======================================================================
        
        #self.lastZones.append(zone)
        self.resizeTableTopAndAddTiles(connector,zone)
        
        for connector in zone.getFreeConnectors():
            self.log.debug('Add zone '+str(connector))
        
            self.addZone(connector, connector.zoneDealer)
        
        
               


        
    def resizeTableTopAndAddTiles(self,connectTo,zone):
        self.log.debug('Direction '+connectTo.direction+', resize, old size '+str(self.sizeX)+'x'+str(self.sizeY)+' with '+str(len(self.tiles))+' tiles')
        self.log.debug('A -- zone have '+str(len(zone.tiles))+' tiles')
        self.log.debug('connectTo:'+str(connectTo))
       
        self.log.debug('zone:'+str(zone))
       
        actualX = connectTo.position1X
        actualY = connectTo.position1Y
        
        self.log.debug('actualX:'+str(actualX))
        self.log.debug('actualY:'+str(actualY))   
              
        compatibleConnector = zone.getCompatibleConnector(connectTo)
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
              
        zone.translate(translateX,translateY)       
        
        self.log.debug('translate zone:'+str(zone))
        
        self.log.debug('B -- zone have '+str(len(zone.tiles))+' tiles')
        
        expandXeast = 0
        expandXwest = 0
        expandYnorth = 0
        expandYsouth = 0 
        
        self.log.debug('startX:'+str(zone.startX))
        self.log.debug('startY:'+str(zone.startY))
        self.log.debug('sizeX:'+str(zone.sizeX))
        self.log.debug('sizeY:'+str(zone.sizeY))
        
        self.log.debug('maxX:'+str(zone.getMaxX()))
        self.log.debug('maxY:'+str(zone.getMaxY()))
        self.log.debug('minX:'+str(zone.getMinX()))
        self.log.debug('minY:'+str(zone.getMinY()))
        
        if zone.getMaxX() > self.sizeX - 1:
            expandXeast =  zone.getMaxX() - ( self.sizeX -1 )
        if zone.getMaxY() > self.sizeY - 1:
            expandYsouth =  zone.getMaxY() - ( self.sizeY -1)
        if zone.getMinX() < 0:
            expandXwest =  abs(zone.getMinX())
        if zone.getMinY() < 0:
            expandYnorth =  abs(zone.getMinY())
        
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
        
        for zoneLoop in self.lastZones:
            zoneLoop.translate(expandXwest,0)
        
        
        self.log.debug('transfert : start')
        #copy old tiles in new tabletop
        for y in range(0,oldSizeY):
            for x in range(0,oldSizeX):
                oldTileIndex = x + (y * oldSizeX)
                #self.log.debug('transfert :'+str(x+abs(expandXwest))+','+str(y))
                self.setTile(oldTiles[oldTileIndex], x+abs(expandXwest), y)
        self.log.debug('transfert : end')
         
        #for lastZone in self.lastZones:
        #    lastZone.translate(expandXwest,expandYnorth)
                
        zone.translate(expandXwest,expandYnorth)
        
        self.log.debug('translate zone:'+str(zone))
        
        self.log.debug('maxX:'+str(zone.getMaxX()))
        self.log.debug('maxY:'+str(zone.getMaxY()))
        self.log.debug('minX:'+str(zone.getMinX()))
        self.log.debug('minY:'+str(zone.getMinY()))
        
        self.log.debug('C -- zone have '+str(len(zone.tiles))+' tiles')
        count = 1

        for y in range(zone.getMinY(),zone.getMaxY()+1):
            for x in range(zone.getMinX(),zone.getMaxX()+1):
                #self.log.debug('['+str(count)+'] Transfer tiles '+str(x)+' '+str(y)+' in '+str(len(self.tiles)))
                targetTile = self.getTile(x, y)
                
                if targetTile == None or targetTile.hasFunction('B'):
                    self.setTile(zone.getTile(x,y), x, y)
                else:
                    raise TileException('Tile conflict @ '+str(x)+'/'+str(y))
                count = count + 1
                
        self.lastZones.append(zone)
        
                
        
        
        
        self.log.debug('New size '+str(self.sizeX)+'x'+str(self.sizeY)+' with '+str(len(self.tiles))+' tiles')
        zone.lockCompatibleConnector(connectTo.direction,connectTo.zoneDealer)         
        
     