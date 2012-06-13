from render import Render
from log4py import Logger

class AsciiRender(Render):
    pass

    def __init__(self):
        self.log = Logger().get_instance(self.__class__.__name__)
        
    
    def renderTabletop(self,tableTop):
        asciiMap = ''
        index=0
        self.log.debug('Tabletop size x:'+str(tableTop.globalWidth)+'  y:'+str(tableTop.globalHeight))
        
        for i in range(0,tableTop.globalHeight):
            for j in range(0,tableTop.globalWidth):
                tile = tableTop.globalTiles[index]
                asciiMap += self.getImageForTile(tile)
                index +=1
            asciiMap += '\n'
        print asciiMap
            
        pass
    
    
    def getImageForTile(self,tile):
        if tile.hasFunction('IO'):
            return '[D]'
        if tile.hasFunction('D'):
            return '[ ]'
        return '   ';