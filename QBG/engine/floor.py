class FloorSizeException(Exception):
    pass

class Floor(object):
    
    
    '''
    Width of floor
    '''
    tilesWidth = 0
    
    '''
    Height of floor
    '''
    tilesHeight = 0
    
    '''
    Tiles list
    '''
    tiles = [] # Tile
    
    
    def __init__(self):
        pass
        
    def toTile(self,tiles):
        for tile in tiles:
            self.addTile(tile)  

    def addTile(self,tile):
        self.tiles.append(tile)
        
    def checkFloorSizes(self):
        totalTiles = self.tilesHeight * self.tilesWidth
        if totalTiles != len(self.tiles) :
            raise FloorSizeException
        

        
         
        