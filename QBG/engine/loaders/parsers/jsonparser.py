from parser import Parser
import json

class JsonParser(Parser):
    
    def __init__(self,fileName):
        Parser.__init__(self,fileName)
        
    def loadInClass(self,className):
        
        fileReader = open(self.fileName)
        
        print json.load(fileReader)
            