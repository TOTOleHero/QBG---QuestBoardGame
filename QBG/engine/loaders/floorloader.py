import re
import os
from log4py import Logger
from loader import Loader
from ..floor import Floor 

class FloorLoader(Loader):

    def __init__(self,directories,tileFunctionLoader):
        Loader.__init__(self)
        '''
        Tile loader for load the good tile
        '''
        self.tileFunctionLoader = tileFunctionLoader
        splitter = re.compile(r'(\s+|\S+)')
        self.directories = splitter.findall(directories)
        self.data = {}
    
    def load(self,data):
        for directory in self.directories:
            if(os.access(directory, os.F_OK)):
                self.loadFiles(directory, os.listdir(directory))
            else:
                self.log.error( directory + ' not exist') 
        data['floor'] = self.data
        for subtype in self.data.iterkeys():
            self.log.info('Exist subtype : '+subtype)
         
    
    def loadFiles(self,directory, filesList):
        
        for file in filesList:
            self.log.debug(file)
            if(os.path.isdir(directory+'/'+file) == False and os.access(directory+'/'+file, os.F_OK)):            
                parser = Loader.loadParserForFile(self,'floor',directory+'/'+file)
                if parser != None:
                    floor = Floor(self.tileFunctionLoader)
                    floor = parser.loadInClass(floor)
                    if not floor.subType in self.data:
                        self.data[floor.subType] = []
                    self.data[floor.subType].append(floor)
                    self.log.info('Floor "'+ floor.name + '" Done')
            
             