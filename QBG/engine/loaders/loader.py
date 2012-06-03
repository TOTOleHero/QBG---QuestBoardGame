import re
from log4py import Logger
import parsers.jsonparser

class Loader(object):
    
    log = None
    
    def __init__(self):
        self.log = Logger().get_instance(self.__class__.__name__)
    
    def loadParserForFile(self,type,file):
        parser = None
        
        tokens = re.split('[.]',file)
        if tokens[1] == type:
            
            # construct parser class
            try:
                parser = {
                'json': parsers.jsonparser.JsonParser(file)
                } [ tokens[2] ]
            except KeyError:
                self.log.warn('Parser '+ tokens[2] + ' not found')
                parser = None
        else:
            self.log.debug('Type '+ tokens[1] + ' ignored')
            
        return parser