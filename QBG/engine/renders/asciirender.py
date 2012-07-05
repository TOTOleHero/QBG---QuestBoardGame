from render import Render
from log4py import Logger

class AsciiRender(Render):
    pass

    def __init__(self):
        self.log = Logger().get_instance(self.__class__.__name__)
        
    
    def renderTabletop(self,tableTop):
        asciiMap = ''
        index=0
        self.log.debug('Tabletop size x:'+str(tableTop.sizeX)+'  y:'+str(tableTop.sizeY))
        
        for i in range(0,tableTop.sizeY):
            for j in range(0,tableTop.sizeX):
                tile = tableTop.tiles[index]
                asciiMap += self.getImageForTile(tile)
                index +=1
            asciiMap += '\n'
        print asciiMap

    
    def renderRoom(self,room):
        asciiMap = ''
        index=0
        self.log.debug('Room size x:'+str(room.sizeX)+'  y:'+str(room.sizeY))
        
        asciiMap += '\n| |'
        
        for x in range(room.getMinX(),room.getMaxX() +1 ):
            asciiMap += '|'+str(x)+'|'
        asciiMap += '\n'
        for y in range(room.getMinY(),room.getMaxY() +1 ):
            asciiMap += '|'+str(y)+'|'
            for x in range(0,room.sizeX):
                tile = room.tiles[index]
                asciiMap += self.getImageForTile(tile)
                index +=1
            asciiMap += '\n'
        return asciiMap
    
    
    def getImageForTile(self,tile):
        if tile != None and tile.hasFunction('IO'):
            return '[D]'
        if tile != None and tile.hasFunction('D'):
            return '[ ]'
        return '___';