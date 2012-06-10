from parser import Parser
import json
import re
import copy

class JsonParser(Parser):
    
    def __init__(self,fileName):
        Parser.__init__(self,fileName)
        
    def loadInClass(self,newObject):
        
        fileReader = open(self.fileName)
        
        dictData = json.load(fileReader)
         
        dictData['objectType'] = self.extractTypeFromFilename(self.fileName) 

        newObject.setDict(dictData)
         
        return newObject  

    def extractTypeFromFilename(self,fileName):
        path = re.split('[/]',fileName)
        tokens = re.split('[.]',path.pop())
        return tokens[0]
        
    
class JsonDictContainer(object):
    
    def setDict(self,dictData):
        
        self.dictData = dictData
        