import re
from log4py import Logger
import parsers.jsonparser
import parsers.pyparser

class Loader(object):
    
    def __init__(self):
        self.log = Logger().get_instance(self.__class__.__name__)
    
    def loadParserForFile(self,objectType,fileName):
        parser = None
        self.log.debug('Want load object of type "'+objectType+'"')
        
        tokens = re.split('[.]',fileName)
        self.log.debug('tokens are : '+str(tokens))
        self.log.debug('check : '+str(tokens[1])+' == '+str(objectType))
        if tokens[1] == objectType:
            
            # construct parser class
            try:
                parser = {
                'json': parsers.jsonparser.JsonParser(fileName)
                ,'py': parsers.pyparser.PyParser(fileName)
                } [ tokens[2] ]
            except KeyError:
                self.log.warn('Parser '+ tokens[2] + ' not found')
                parser = None
        else:
            self.log.debug('Type '+ tokens[1] + ' ignored')
            
        return parser
    
