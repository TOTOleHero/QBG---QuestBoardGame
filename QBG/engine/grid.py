from connector import Connector
from log4py import Logger
from tile import Tile
import copy

'''
Exception raise if size of grid is not compatible with number of tile
'''
class GridSizeException(Exception):
    pass

'''
Grid with X and Y position (origin is at the top-left)
'''
class Grid(object):
    
    def __init__(self):
        #self.log = Logger().get_instance(self.__class__.__name__)
        self.sizeX = 0
        self.sizeY = 0
        self.tiles = []
    
    
    
    '''
    rotate all tiles in grid
    '''    
    def rotate(self):
        #self.log.debug('Rotate '+self.name+' left. '+str(len(self.tiles))+' of '+str(self.sizeX)+'/'+str(self.sizeY))
        newTiles = []
        
        for x in range(0,self.sizeX):
            #need to reverse tiles reader in y axis
            for y in range((self.sizeY -1),-1,-1):
                newTiles.append( self.tiles[x + (y * self.sizeX)])
        self.tiles = newTiles
        x = self.sizeX
        self.sizeX = self.sizeY
        self.sizeY = x
        #self.log.debug('After rotate '+self.name+' left. '+str(len(self.tiles))+' of '+str(self.sizeX)+'/'+str(self.sizeY))
        
    '''
    Check if the grid have X and Y compatible with her tiles number
    ''' 
    def checkGridSizes(self):
        totalTiles = self.sizeY * self.sizeX
        if totalTiles != len(self.tiles) :
            raise GridSizeException('size '+str(self.sizeX)+' by '+str(self.sizeY)+' not match with tiles total :'+str(len(self.tiles)))
    
    '''
    Get tile at position X/Y
    '''   
    def getTile(self,x,y):
        #self.log.debug('sizeX: '+str(self.sizeX)+'/sizeY:'+str(self.sizeY))
        
        indexTile = (x + y * self.sizeX)
        #self.log.debug('getTile @ '+str(x) +' '+str(y)+' @index:'+str(indexTile)+' in '+str(len(self.tiles))+' tiles')
        return self.tiles[indexTile]    
    
    '''
    Set tile at position X/Y
    '''
    def setTile(self,tile,x,y):
        #self.log.debug('setTile @ '+str(x)+' '+str(y)+' grid size '+str(self.sizeX)+' '+str(self.sizeY))
        self.tiles[x + (y * self.sizeX)] = tile
    
    def resetGrid(self):
        #self.log.debug('resetGrid to '+str(self.sizeX)+' '+str(self.sizeY))
        self.tiles = []
        for i in range(0, self.sizeX * self.sizeY):
            self.tiles.append(None)


                
            
            
            
            