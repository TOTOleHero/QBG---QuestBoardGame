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
        self.log = Logger().get_instance(self.__class__.__name__)
        self.sizeX = 0
        self.sizeY = 0
        self.tiles = []
    
    '''
    rotate all tiles in grid
    '''    
    def rotate(self):
        self.log.debug('Rotate '+self.name+' left')
        newTiles = []
        j = 0
        for i in range(0,self.sizeX):
            for j in range(0,self.sizeY):
                newTiles.append( self.tiles[i + (j * self.sizeX)])
        self.tiles = newTiles

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
        return self.tiles[(x + y * self.sizeX)]    
    
    '''
    Set tile at position X/Y
    '''
    def setTile(self,tile,x,y):
        pass
    
    def resetGrid(self):
        for i in range(0, self.sizeX * self.sizeY):
            self.tiles.append(None)