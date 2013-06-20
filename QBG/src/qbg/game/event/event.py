# To change this template, choose Tools | Templates
# and open the template in the editor.

from log4py import Logger
from qbg.config.loaders.loadable import Loadable

__author__="Thomas Lecarpentier / TOTOleHero <thomas.lecarpentier+coder[at]gmail.com>"
__date__ ="$20 juin 2013 19:01:57$"


class Event(Loadable):
    
    def __init__(self,eventName=None):
        self.log = Logger().get_instance(self.__class__.__name__)
        self.eventName = eventName
        self.eventParameters = []
        
    def setDict(self,dictData):
        self.log.debug(str(dictData))
        self.eventName = dictData['eventName']
        self.eventParameters = dictData['eventParameters'] 

