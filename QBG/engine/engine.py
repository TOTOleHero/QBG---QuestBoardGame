import random
import copy
from log4py import Logger
from tabletop import TableTop

class Engine(object):
    
    
    
    def __init__(self):
        self.log = Logger().get_instance(self.__class__.__name__)
        self.loaders = []    
        self.data = {}
        self.donjonSubTypeCount = {}
        self.generateDongeonArray = []
        self.renderObject = None
        self.tableTop = TableTop()
    
    def load(self):
        
        for loader in self.loaders:
            loader.load(self.data)
            print loader.__class__.__name__ + ' Finished'
        print 'Run loaders Finished'
    
    
    def authorizeDungeonSubTypeCount(self,subType, count):
        if subType in self.data['floor']:
            self.donjonSubTypeCount[subType] = count
        
    def addLoader(self,loader):
        self.loaders.append(loader)
    
    def setRender(self,render):
        self.renderObject = render
    
    def render(self):
        self.tableTop.addFloor(self.generateDongeonArray[0])
        self.tableTop.addFloor(self.generateDongeonArray[1])
        self.renderObject.renderTabletop(self.tableTop)
        
    def generateDongeon(self):
        
        for index,value in self.donjonSubTypeCount.iteritems():
            for i in range(0,value):
                self.generateDongeonArray.append(self.takeOneRandomFloorOfType(index,value - i))
        
        random.shuffle(self.generateDongeonArray)
        self.pushObjectiveRoomToDeep(self.generateDongeonArray)
        
        
        
    def takeOneRandomFloorOfType(self,subType,countAgain):
        tempArray = self.data['floor'][subType]
        
        if not self.hasNonUniqueFloor(tempArray):
            if len(tempArray) < countAgain:
                raise Exception('There are not enought floor subtype ' +subType+ '. rest '+str(len(tempArray))+' needed '+str(countAgain))
        
        random.shuffle(tempArray)
        if tempArray[0].unique:
            uniqueFloor = tempArray[0]
            tempArray.remove(uniqueFloor)
            return uniqueFloor
        else:
            return copy.copy(tempArray[0])
        
    def pushObjectiveRoomToDeep(self,generateDongeon):
        for floor in generateDongeon:
            if floor.subType == 'objective-room':
                generateDongeon.remove(floor)
                countItems = len(generateDongeon)
                afterMiddle = countItems / 2
                self.log.debug('push objective room after '+str(afterMiddle)+' index')
                randomIndex = random.randrange(afterMiddle,countItems)
                generateDongeon.insert(randomIndex,floor)
                break
     
    def hasNonUniqueFloor(self,floors):
        for floor in floors:
            if not floor.unique:
                return True           
        
        
        
        
        
        
        
        
        
        
        
        
            
        