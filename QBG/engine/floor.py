from loaders.parsers.jsonparser import JsonDictContainer
from log4py import Logger
from tile import Tile

class FloorSizeException(Exception):
    pass

class FloorConnectorException(Exception):
    pass

class FloorTypeException(Exception):
    pass

class Floor(JsonDictContainer):

    def __init__(self,tileFunctionLoader):
        self.log = Logger().get_instance(self.__class__.__name__)
        '''
        Tile loader able to interprete tile CODE
        '''
        self.tileFunctionLoader = tileFunctionLoader
               
        '''
        Width of floor
        '''
        self.tilesWidth = 0
        
        '''
        Height of floor
        '''
        self.tilesHeight = 0
        
        '''
        Tiles list
        '''
        self.tiles = [] # Tile
        
        '''
        Name of floor
        '''
        self.name = ''
        
        '''
        Type of this floor, type is define in data filename <type>.<class>.<parser>
        '''
        self.objectType = ''
        self.subType = None
                
        
    def toTile(self,tiles):
        for tile in tiles:
            self.addTile(tile)  

    def addTile(self,tileDefinition):
        newTile = Tile()
        newTile.floor = self
        newTile.setFunctions(self.tileFunctionLoader.getTileFunctionFromDefinition(tileDefinition))
        self.log.debug(self.name +' have ' +str(len(self.tiles))+ ' tiles')
        self.tiles.append(newTile)
        
    def addLine(self,lineDefinition):
        self.log.debug('tiles definition elements : ' + str(len(lineDefinition)))
        for tileDefinition in lineDefinition:
            self.addTile(tileDefinition)
            if self.tilesHeight == None:
                self.tilesWidth += 1
    
    def setDefinition(self,definition): 
        self.tilesWidth = 0
        self.tilesHeight = None
        self.log.debug(str(len(definition)) + ' line definition')
        for lineDefinition in definition:
            self.addLine(lineDefinition)
            if self.tilesHeight == None:
                self.tilesHeight = 0
            self.tilesHeight+= 1       
             
    def checkFloorSizes(self):
        totalTiles = self.tilesHeight * self.tilesWidth
        if totalTiles != len(self.tiles) :
            raise FloorSizeException('size '+str(self.tilesWidth)+' by '+str(self.tilesHeight)+' not match with tiles total :'+str(len(self.tiles)))
    
    def setDict(self,dictData):
            self.log.debug(str(dictData))
            self.objectType = dictData['objectType']
            self.name = dictData['name']
            self.setDefinition(dictData['definition'])
            self.subType = dictData['subType']  
            
            
        
         
        