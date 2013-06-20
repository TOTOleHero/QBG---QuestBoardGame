import re
import os
from log4py import Logger
from qbg.config.loaders.loader import Loader
from qbg.characters.character import *
from qbg.characters.hero import *
from qbg.characters.monster import *


class CharacterLoader(Loader):
    
    def __init__(self,directories,itemLoader):
        Loader.__init__(self)
        '''
        character loader for load the good item
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
        data['character'] = self.data
        for subtype in self.data.iterkeys():
            self.log.info('Exist subtype : '+subtype)
         
    
    def loadFiles(self,directory, filesList):
        
        for file in filesList:
            self.log.debug(file)
            if(os.path.isdir(directory+os.sep+file) == False and os.access(directory+os.sep+file, os.F_OK)):            
                parser = Loader.loadParserForFile(self,'character',directory+os.sep+file)
                if parser != None:
                    character = Character(self.itemsLoader)
                    character = parser.loadInClass(character)
                    
                    if character._type == character.TYPE_HERO:
                        self.log.debug('Change class to Hero')
                        character.__class__ = Hero
                    elif character._type == character.TYPE_MONSTER:
                        self.log.debug('Change class to Monster')
                        character.__class__ = Monster
                    
                    if not character._name in self.data:
                        self.data[character._name] = []
                    self.data[character._name].append(character)
                    self.log.info('character "'+ character._name + '" Done')
            
             