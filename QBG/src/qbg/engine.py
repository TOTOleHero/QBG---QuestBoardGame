import random
import copy
from log4py import Logger
from qbg.game.space.tabletop import TableTop
from zonedealer import ZoneDealer

class Engine(object):
        
    
    def __init__(self):
        self.log = Logger().get_instance(self.__class__.__name__)
        self.loaders = []    
        self.data = {}
        self.donjonSubTypeCount = {}
        self.generateDongeonArray = []
        self.renderObject = None
        self.tableTop = TableTop()
        self.firstZoneDealer = None
    
    
    def load(self):
        
        for loader in self.loaders:
            loader.load(self.data)
            self.log.info(loader.__class__.__name__ + ' Finished')
        print 'Run loaders Finished'
    
    
    def authorizeDungeonSubTypeCount(self, subType, count):
        if subType in self.data['zone']:
            self.donjonSubTypeCount[subType] = count
        
    def addLoader(self, loader):
        self.loaders.append(loader)
    
    def setRender(self, render):
        self.renderObject = render
    
    def render(self):
        
        #=======================================================================
        # self.tableTop.addZone(self.generateDongeonArray[0])
        # self.renderObject.renderTabletop(self.tableTop)
        # self.tableTop.addZone(self.generateDongeonArray[1])
        # self.renderObject.renderTabletop(self.tableTop)
        # self.tableTop.addZone(self.generateDongeonArray[2])
        # self.renderObject.renderTabletop(self.tableTop)
        # self.tableTop.addZone(self.generateDongeonArray[3])
        # self.renderObject.renderTabletop(self.tableTop)
        # self.tableTop.addZone(self.generateDongeonArray[4])
        #=======================================================================
        
        
        self.log.debug(str(self.firstZoneDealer))
        
        self.tableTop.initialConnector.zoneDealer = self.firstZoneDealer
        
        self.tableTop.addZone(self.tableTop.initialConnector,self.firstZoneDealer)
        
        self.renderObject.renderTabletop(self.tableTop)
        
        
        
    def generateDongeon(self):
        zoneDealer = ZoneDealer()
        generateDongeonArray = []
        for objectType, value in self.donjonSubTypeCount.iteritems():
            for i in range(0, value):
                generateDongeonArray.append(self.takeOneRandomZoneOfType(objectType, value - i))
        
        random.shuffle(generateDongeonArray)
        self.pushObjectiveZoneToDeep(generateDongeonArray)
        
        for zone in generateDongeonArray:
            zoneDealer.addZone(zone)
            
        self.firstZoneDealer = zoneDealer
        
        
    def takeOneRandomZoneOfType(self, subType, countAgain):
        tempArray = self.data['zone'][subType]
        
        self.log.debug('data for '+subType+':'+ str(tempArray))
        
        if not self.hasNonUniqueZone(tempArray):
            if len(tempArray) < countAgain:
                raise Exception('There are not enougth zone subtype ' + subType + '. rest ' + str(len(tempArray)) + ' needed ' + str(countAgain))
        
        random.shuffle(tempArray)
        if tempArray[0].unique:
            uniqueZone = tempArray[0]
            tempArray.remove(uniqueZone)
            return uniqueZone
        else:
            return copy.deepcopy(tempArray[0])
        
    def pushObjectiveZoneToDeep(self, generateDongeon):
        for zone in generateDongeon:
            if zone.subType == 'objective-zone':
                generateDongeon.remove(zone)
                countItems = len(generateDongeon)
                afterLimit = (countItems / 3) # * 2
                self.log.debug('push objective zone after ' + str(afterLimit) + ' index')
                randomIndex = random.randrange(afterLimit, countItems)
                self.log.debug('push objective zone in ' + str(randomIndex) + ' index')
                generateDongeon.insert(randomIndex, zone)
                break
     
    def hasNonUniqueZone(self, zones):
        for zone in zones:
            if not zone.unique:
                return True           
        
        
        
        
        
        
        
        
        
        
        
        
            
        
