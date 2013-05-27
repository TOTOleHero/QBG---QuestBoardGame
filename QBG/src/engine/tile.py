from log4py import Logger
from direction import Direction

class Tile(object):
    
    
    def __init__(self):
        self.log = Logger().get_instance(self.__class__.__name__)
        self.room = None
        self.functions = []
        self.contiguous = {}
        self.contiguous['south'] = None 
        self.contiguous['north'] = None 
        self.contiguous['east'] = None 
        self.contiguous['west'] = None 
   
    def addFunction(self,function):
        self.functions.append(function)
        
    def setFunctions(self,functions):
        self.functions = functions
        self.log.debug(str(self.functions))
  
    def hasFunction(self,code):
        for function in self.functions:
            if function.code == code:
                return True
        return False
    
    def hasNeighbor(self,direction):
        return self.contiguous[direction] != None
    
    def countNeighbor(self):
        direction = ''
        count = 0
        if self.contiguous['south'] != None:
            direction = direction + 'S'
            count = count + 1
        else:
            direction = direction + ' '
            
        if self.contiguous['north'] != None:
            direction = direction + 'N'
            count = count + 1
        else:
            direction = direction + ' '
        if self.contiguous['east'] != None:
            direction = direction + 'E'
            count = count + 1
        else:
            direction = direction + ' '
        if self.contiguous['west'] != None:
            direction = direction + 'W'
            count = count + 1
        else:
            direction = direction + ' '
        self.log.debug('['+direction+']')
        return count
         
    def addTileNeighborAt(self,tile,direction):
        if self == tile:
            raise Exception('Stop, i can''t be my Neighbor')
        compatibleDirection = Direction.directionCompatibility[direction]
        
        if not (self.hasFunction('B') or tile.hasFunction('B')) :
            self.contiguous[direction]=tile
            tile.contiguous[compatibleDirection]=self
        
        #self.log.debug('Me '+ str(self.functions[0].name)+', i have '+ str(self.countNeighbor())+ ' Neighbor')
        #self.log.debug('Other '+ str(tile.functions[0].name)+',it have '+ str(tile.countNeighbor())+ ' Neighbor')
        
  
class TileFunction:

    def __init__(self):
        self.log = Logger().get_instance(self.__class__.__name__)
        self.name = ''
        self.objectType = ''
        self.code = ''
    
    def setDict(self,dictData):
        self.log.debug(str(dictData))
        self.name = dictData['name']
        self.objectType = dictData['objectType'] 
        
        self.code = dictData['code']  

    
