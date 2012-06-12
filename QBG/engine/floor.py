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
        self.unique = False
        self.connectors = {}
        self.connectorCompatibility = {'north':'south', 'south':'north', 'east':'west', 'west':'east'}
                
        
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
            self.unique = dictData['unique']  
            self.createConnector()
        
    def createConnector(self):
        io1 = False
        io2 = False        
        #north detection        
        for i in range(0,self.tilesWidth):
                detectTile = self.tiles[i]
                if detectTile.hasFunction('IO'):
                    if not io1:
                        io1 = True
                    if io1:
                        io2 = True
                    if io1 and io2:
                        raise Exception('more than one IO for north side')
        if io1 and io2:
            self.connectors['north'] = True
            
        
        io1 = False
        io2 = False        
        #south detection        
        for i in range(0,self.tilesWidth):
                detectTile = self.tiles[i+self.tilesHeight]
                if detectTile.hasFunction('IO'):
                    if not io1:
                        io1 = True
                    if io1:
                        io2 = True
                    if io1 and io2:
                        raise Exception('more than one IO for north side')
        if io1 and io2:
            self.connectors['south'] = True    
            
        
        io1 = False
        io2 = False        
        #west detection        
        for i in range(0,self.tilesHeight):
                detectTile = self.tiles[i * self.tilesWidth]
                if detectTile.hasFunction('IO'):
                    if not io1:
                        io1 = True
                    if io1:
                        io2 = True
                    if io1 and io2:
                        raise Exception('more than one IO for west side')
        if io1 and io2:
            self.connectors['west'] = True
                     
        io1 = False
        io2 = False        
        #east detection        
        for i in range(0,self.tilesHeight):
                detectTile = self.tiles[(i * self.tilesWidth) + self.tilesWidth]
                if detectTile.hasFunction('IO'):
                    if not io1:
                        io1 = True
                    if io1:
                        io2 = True
                    if io1 and io2:
                        raise Exception('more than one IO for east side')
        if io1 and io2:
            self.connectors['east'] = True
        
        
            
    def lockConnector(self,direction):
        if not self.connectors[direction]:
            raise Exception('Connector '+direction + ' already connected')
        self.connectors[direction] = False     
    
    def hasFreeConnector(self,direction = None):
        if direction == None:
            for connector,free in self.connectors.iteritems():
                if free:
                    return  free

        else:
            for connector,free in self.connectors.iteritems():
                    if connector == direction:
                        if free:
                            return free
        return False
    
    
    def getCompatibleDirection(self,direction):
        return self.connectorCompatibility[direction]    
                 
    def getFreeConnectors(self):
        freeConnectors = []
        for connector,free in self.connectors.items():
            if free:
                freeConnectors.append(connector) 
        return freeConnectors
    
    def rotateForCompatibleConnector(self,connector):
        
        for i in range(4):
            if not self.hasFreeConnector(self.getCompatibleDirection(connector)):
                self.rotate()
            else:
                return True
        
        return False                   
    
    def rotate(self):
        newTiles = []
        j = 0
        for i in range(0,self.tilesWidth):
            for j in range(0,self.tilesHeight):
                newTiles.append( self.tiles[i + (j * self.tilesWidth)])
        print newTiles
           
            
                  
            
            
         
        