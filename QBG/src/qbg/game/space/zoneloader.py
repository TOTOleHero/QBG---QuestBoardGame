import re
import os
from log4py import Logger
from qbg.config.loaders.loader import Loader
from qbg.game.space.zone import Zone 

class ZoneLoader(Loader):

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
        data['zone'] = self.data
        for subtype in self.data.iterkeys():
            self.log.info('Exist subtype : '+subtype)
         
    
    def loadFiles(self,directory, filesList):
        
        for file in filesList:
            self.log.debug(file)
            if(os.path.isdir(directory+'/'+file) == False and os.access(directory+'/'+file, os.F_OK)):            
                parser = Loader.loadParserForFile(self,'zone',directory+'/'+file)
                if parser != None:
                    zone = Zone(self.tileFunctionLoader)
                    zone = parser.loadInClass(zone)
                    if not zone.subType in self.data:
                        self.data[zone.subType] = []
                    self.data[zone.subType].append(zone)
                    self.log.info('Zone "'+ zone.name + '" Done')
            
             