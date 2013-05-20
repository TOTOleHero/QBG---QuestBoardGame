import re
import os
from log4py import Logger
from loader import Loader
from ..creature import Creature 
from ..character import *


class CreatureLoader(Loader):
    
    def __init__(self,directories,itemLoader):
        Loader.__init__(self)
        '''
        Creature loader for load the good item
        '''
        self.itemsLoader = itemLoader
        splitter = re.compile(r'(\s+|\S+)')
        self.directories = splitter.findall(directories)
        self.data = {}
    
    def load(self,data):
        for directory in self.directories:
            if(os.access(directory, os.F_OK)):
                self.loadFiles(directory, os.listdir(directory))
            else:
                self.log.error( directory + ' not exist') 
        data['creature'] = self.data
        for subtype in self.data.iterkeys():
            self.log.info('Exist subtype : '+subtype)
         
    
    def loadFiles(self,directory, filesList):
        
        for file in filesList:
            self.log.debug(file)
            if(os.path.isdir(directory+'/'+file) == False and os.access(directory+'/'+file, os.F_OK)):            
                parser = Loader.loadParserForFile(self,'creature',directory+'/'+file)
                if parser != None:
                    creature = Creature(self.itemsLoader)
                    creature = parser.loadInClass(creature)
                    
                    if creature._type == Creature.TYPE_HERO:
                        self.log.debug('Change class to Hero')
                        creature.__class__ = Hero
                    elif creature._type == Creature.TYPE_MONSTER:
                        self.log.debug('Change class to Monster')
                        creature.__class__ = Monster
                    
                    if not creature._name in self.data:
                        self.data[creature._name] = []
                    self.data[creature._name].append(creature)
                    self.log.info('Creature "'+ creature._name + '" Done')
            
             