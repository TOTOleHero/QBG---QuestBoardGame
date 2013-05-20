import re
import copy
import os
from log4py import Logger
from loader import Loader
from ..item import Item

class ItemLoader(Loader):
        
    def __init__(self,directories):
        Loader.__init__(self)
        splitter = re.compile(r'(\s+|\S+)')
        self.directories = splitter.findall(directories)
        self.data = []
        pass
    
    def load(self,data):
        for directory in self.directories:
            if(os.access(directory, os.F_OK)):
                self.loadFiles(directory, os.listdir(directory))
            else:
                self.log.error( directory + ' not exist') 
         
    
    def loadFiles(self,directory, filesList):
        
        for file in filesList:
            self.log.debug(file)
            parser = Loader.loadParserForFile(self,'item',directory+'/'+file)
            if parser != None:
                self.data.append(parser.loadInClass(Item()))
    
    def getItemFromCode(self,code):  
        for item in self.data:
                if item.code == code:
                    return copy.deepcopy(item)
        return None
    
    def getItemFromDefinition(self,codes):  
        self.log.debug('Tiles code '+str(codes))
        
        returnItems = []
        
        for code in codes:
            item = self.getItemFromCode(code)
            if item != None:
                returnItems.append(function)        
            
        return returnItems
              
             