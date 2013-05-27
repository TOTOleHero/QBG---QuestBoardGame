from parser import Parser
import re

class PyParser(Parser):
    
    def __init__(self,fileName):
        Parser.__init__(self,fileName)
        
    def loadInClass(self,newObject):
        
        fileReader = open(self.fileName)
        
        fileContent = fileReader.read()
        
        self.log.debug(fileContent)
        
        myDict = eval(fileContent) 
        myDict['objectType'] = self.extractTypeFromFilename(self.fileName) 
         
        newObject.setDict(myDict)
         
        return newObject  

    def extractTypeFromFilename(self,fileName):
        path = re.split('[/]',fileName)
        tokens = re.split('[.]',path.pop())
        return tokens[0]
        
    
class JsonDictContainer(object):
    
    dictData = None
    
    def setDict(self,dictData):
        
        self.dictData = dictData
        