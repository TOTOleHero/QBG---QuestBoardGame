class Connector(object):
    
    
    def __init__(self,zone):
        self.position1X = None
        self.position1Y = None
        self.position2X = None
        self.position2Y = None
        self.direction = None
        self.locked = False
        self.zone = zone
        self.zoneDealer = None
        
    def getPositionX(self):
        if self.position1X == self.position2X:
            return self.position1X
        else:
            raise Exception('X position not equals')
        
    def getPositionY(self):
        if self.position1Y == self.position2Y:
            return self.position1Y
        else:
            raise Exception('Y position not equals')
         
        
    def __str__(self, *args, **kwargs):
        connectorString = 'Connector : ' + self.direction  
        connectorString += ' @('+str(self.position1X)+','+str(self.position1Y)+')('+str(self.position2X)+','+str(self.position2Y)+')'
        if self.zone != None :
            connectorString += ' of zone : '+self.zone.name
        else:
            connectorString += ' of NO zone '
            
            
        if self.zoneDealer != None :
            connectorString += ' zoneDealer OK'
        else:
            connectorString += ' zoneDealer NULL '   
        return connectorString
    
    def acquire_item(self, item):
        '''
        Acquire an item
        '''
        self._items.append(item)

    def equip(self, item):
        '''
        equip an item
        '''
        item.equip(self)