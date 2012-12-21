import random
import copy
from log4py import Logger
from tabletop import TableTop
from roomdealer import RoomDealer

class Engine(object):
        
    
    def __init__(self):
        self.log = Logger().get_instance(self.__class__.__name__)
        self.loaders = []    
        self.data = {}
        self.donjonSubTypeCount = {}
        self.generateDongeonArray = []
        self.renderObject = None
        self.tableTop = TableTop()
        self.firstRoomDealer = None
    
    
    def load(self):
        
        for loader in self.loaders:
            loader.load(self.data)
            print loader.__class__.__name__ + ' Finished'
        print 'Run loaders Finished'
    
    
    def authorizeDungeonSubTypeCount(self, subType, count):
        if subType in self.data['room']:
            self.donjonSubTypeCount[subType] = count
        
    def addLoader(self, loader):
        self.loaders.append(loader)
    
    def setRender(self, render):
        self.renderObject = render
    
    def render(self):
        
        #=======================================================================
        # self.tableTop.addRoom(self.generateDongeonArray[0])
        # self.renderObject.renderTabletop(self.tableTop)
        # self.tableTop.addRoom(self.generateDongeonArray[1])
        # self.renderObject.renderTabletop(self.tableTop)
        # self.tableTop.addRoom(self.generateDongeonArray[2])
        # self.renderObject.renderTabletop(self.tableTop)
        # self.tableTop.addRoom(self.generateDongeonArray[3])
        # self.renderObject.renderTabletop(self.tableTop)
        # self.tableTop.addRoom(self.generateDongeonArray[4])
        #=======================================================================
        
        
        self.log.debug(str(self.firstRoomDealer))
        
        self.tableTop.initialConnector.roomDealer = self.firstRoomDealer
        
        self.tableTop.addRoom(self.tableTop.initialConnector,self.firstRoomDealer)
        self.renderObject.renderTabletop(self.tableTop)
        
        
        
    def generateDongeon(self):
        roomDealer = RoomDealer()
        generateDongeonArray = []
        for objectType, value in self.donjonSubTypeCount.iteritems():
            for i in range(0, value):
                generateDongeonArray.append(self.takeOneRandomRoomOfType(objectType, value - i))
        
        random.shuffle(generateDongeonArray)
        self.pushObjectiveRoomToDeep(generateDongeonArray)
        
        for room in generateDongeonArray:
            roomDealer.addRoom(room)
            
        self.firstRoomDealer = roomDealer
        
        
    def takeOneRandomRoomOfType(self, subType, countAgain):
        tempArray = self.data['room'][subType]
        
        self.log.debug('data for '+subType+':'+ str(tempArray))
        
        if not self.hasNonUniqueRoom(tempArray):
            if len(tempArray) < countAgain:
                raise Exception('There are not enougth room subtype ' + subType + '. rest ' + str(len(tempArray)) + ' needed ' + str(countAgain))
        
        random.shuffle(tempArray)
        if tempArray[0].unique:
            uniqueRoom = tempArray[0]
            tempArray.remove(uniqueRoom)
            return uniqueRoom
        else:
            return copy.deepcopy(tempArray[0])
        
    def pushObjectiveRoomToDeep(self, generateDongeon):
        for room in generateDongeon:
            if room.subType == 'objective-room':
                generateDongeon.remove(room)
                countItems = len(generateDongeon)
                afterLimit = (countItems / 3) * 2
                self.log.debug('push objective room after ' + str(afterLimit) + ' index')
                randomIndex = random.randrange(afterLimit, countItems)
                self.log.debug('push objective room in ' + str(randomIndex) + ' index')
                generateDongeon.insert(randomIndex, room)
                break
     
    def hasNonUniqueRoom(self, rooms):
        for room in rooms:
            if not room.unique:
                return True           
        
        
        
        
        
        
        
        
        
        
        
        
            
        
