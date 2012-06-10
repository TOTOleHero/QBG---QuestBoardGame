from loaders.parsers.jsonparser import JsonDictContainer
from log4py import Logger

class Tile(JsonDictContainer):
    
    
    def __init__(self):
        self.log = Logger().get_instance(self.__class__.__name__)
        self.floor = None
        self.functions = []
   
    def setFunctions(self,functions):
        self.functions = functions
  
class TileFunction:

    def __init__(self):
        self.log = Logger().get_instance(self.__class__.__name__)
    
    def setDict(self,dictData):
        self.log.debug(str(dictData))
        self.name = dictData['name']
        self.objectType = dictData['objectType'] 
        
        self.code = dictData['code']  

    
