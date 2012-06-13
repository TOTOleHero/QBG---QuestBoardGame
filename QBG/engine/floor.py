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
        self.tiles.append(newTile)
        self.log.debug(self.name +' have ' +str(len(self.tiles))+ ' tiles')
        
    def addLine(self,lineDefinition):
        self.log.debug('tiles definition elements for '+self.name+' : ' + str(len(lineDefinition)))
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
        self.connectors = {}
        
        io1 = False
        io2 = False
        checkNext = False        
        #north detection        
        for i in range(0,self.tilesWidth):
            self.log.debug('north check tile index : '+str(i))    
            detectTile = self.tiles[i]
            if detectTile.hasFunction('IO') and not io1:
                io1 = True
                checkNext = True
            elif detectTile.hasFunction('IO') and io1 and checkNext:
                io2 = True
            else:
                io1 = False
                io2 = False
                checkNext = False 
                    
            if io1 and io2:
                self.connectors['north'] = True
                self.log.debug('north detected')
            
        
        io1 = False
        io2 = False 
        checkNext = False        
        #south detection        
        for i in range(0,self.tilesWidth):
            self.log.debug('south check tile index : '+str(i+(self.tilesHeight*self.tilesWidth)-self.tilesWidth)) 
            detectTile = self.tiles[i+(self.tilesHeight*self.tilesWidth)-self.tilesWidth]

            if detectTile.hasFunction('IO') and not io1:
                io1 = True
                checkNext = True
            elif detectTile.hasFunction('IO') and io1 and checkNext:
                io2 = True
            else:
                io1 = False
                io2 = False
                checkNext = False 

            if io1 and io2:
                self.connectors['south'] = True
                self.log.debug('south detected')    
            
        
        io1 = False
        io2 = False  
        checkNext = False       
        #west detection        
        for i in range(0,self.tilesHeight):
            self.log.debug('west check tile index : '+str(i * self.tilesWidth)) 
            detectTile = self.tiles[i * self.tilesWidth]
            if detectTile.hasFunction('IO') and not io1:
                io1 = True
                checkNext = True
            elif detectTile.hasFunction('IO') and io1 and checkNext:
                io2 = True
            else:
                io1 = False
                io2 = False
                checkNext = False 
                    
            if io1 and io2:
                self.connectors['west'] = True
                self.log.debug('west detected')
                         
        io1 = False
        io2 = False  
        checkNext = False       
        #east detection        
        for i in range(0,self.tilesHeight):
            self.log.debug('east check tile index : '+str((i * self.tilesWidth) + self.tilesWidth-1)) 
            detectTile = self.tiles[(i * self.tilesWidth) + self.tilesWidth-1]
            if detectTile.hasFunction('IO') and not io1:
                io1 = True
                checkNext = True
            elif detectTile.hasFunction('IO') and io1 and checkNext:
                io2 = True
            else:
                io1 = False
                io2 = False
                checkNext = False 

            if io1 and io2:
                self.connectors['east'] = True
                self.log.debug('east detected') 
        
            
    def lockConnector(self,direction):
        self.log.debug('available connectors '+str(self.getFreeConnectors()))    
        if not direction in self.connectors:
            raise Exception('Connector '+direction + ' not exist')
        if not self.connectors[direction]:
            raise Exception('Connector '+direction + ' already connected')
        self.connectors[direction] = False
        self.log.debug('lock direction '+direction+' rest : ' +str(self.getFreeConnectors()))     
    
    def lockCompatibleConnector(self,direction):
        self.lockConnector(self.getCompatibleDirection(direction))
    
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
        self.log.debug('Compatible connector is '+self.connectorCompatibility[direction])
        return self.connectorCompatibility[direction]    
                 
    def getFreeConnectors(self):
        freeConnectors = []
        for connector,free in self.connectors.items():
            if free:
                freeConnectors.append(connector) 
        self.log.debug(self.name + ' has free connectors :'+str(freeConnectors))
        return freeConnectors
    
    def getOneFreeConnector(self):
        return self.getFreeConnectors()[0]
    
    
    def rotateForCompatibleConnector(self,connector):
        for i in range(4):
            self.log.debug('free connectors '+str(self.getFreeConnectors())+ ',Rotate '+str(i)+' times')
            if not self.hasFreeConnector(self.getCompatibleDirection(connector)):
                self.log.debug('not compatible => rotate')
                self.rotate()
            else:
                return True
        
        return False                   
    
    def rotate(self):
        self.log.debug('Rotate '+self.name+' left')
        newTiles = []
        j = 0
        for i in range(0,self.tilesWidth):
            for j in range(0,self.tilesHeight):
                newTiles.append( self.tiles[i + (j * self.tilesWidth)])
        self.tiles = newTiles
        self.createConnector()
           
            
                  
            
            
         
        