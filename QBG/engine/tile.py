from loaders.parsers.jsonparser import JsonDictContainer
from log4py import Logger

class Tile(JsonDictContainer):
    
    
    def __init__(self):
        self.log = Logger().get_instance(self.__class__.__name__)
        self.floor = None
        self.functions = []
   
    def addFunction(self,function):
        self.functions.append(function)
        
    def setFunctions(self,functions):
        self.functions = functions
        self.log.debug(str(self.functions))
  
    def hasFunction(self,code):
        for function in self.functions:
            if function.code == code:
                return True
        return False
  
class TileFunction:

    def __init__(self):
        self.log = Logger().get_instance(self.__class__.__name__)
        self.name = ''
        self.objectType = ''
        self.code = ''
    
    def setDict(self,dictData):
        self.log.debug(str(dictData))
        self.name = dictData['name']
        self.objectType = dictData['objectType'] 
        
        self.code = dictData['code']  

    
