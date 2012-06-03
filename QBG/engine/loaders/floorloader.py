import re
import os
from log4py import Logger
from loader import Loader
from ..floor import Floor 

class FloorLoader(Loader):
    
    directories = []
 
        
    def __init__(self,directories):
        Loader.__init__(self)
        splitter = re.compile(r'(\s+|\S+)')
        self.directories = splitter.findall(directories)
        pass
    
    def load(self):
        for directory in self.directories:
            if(os.access(directory, os.F_OK)):
                self.loadFiles(directory, os.listdir(directory))
            else:
                self.log.error( directory + ' not exist') 
            
        pass 
    
    def loadFiles(self,directory, filesList):
        
        for file in filesList:
            self.log.debug(file)
            parser = Loader.loadParserForFile(self,'floor',directory+'/'+file)
            if parser != None:
                floor = parser.loadInClass(Floor())
            
             