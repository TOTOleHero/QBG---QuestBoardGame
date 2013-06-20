from log4py import Logger

class ZoneDealer:
    
    def __init__(self,zones = []):
        self.log = Logger().get_instance(self.__class__.__name__)
        self.zones = zones
    
    def addZone(self,zone):
        self.log.debug('Add zone '+zone.name)
        self.zones.append(zone)
    
    def getAndRemoveZone(self):
        if len(self.zones) > 0:
            zone = self.zones.pop()
            zone.zoneDealer = self
            return zone
    
    def split(self,count):
        split = {}
        if count == 0:
            return None
        elif count == 1:
            split[0] = self

        else:
            for i in range(0,count):
                split[i] = []
            
            index = 0
            for zone in self.zones:
                split[index].append(zone)
                index = index + 1
                if index == count:
                    index=0
            
            for i in range(0,count):
                split[i] = ZoneDealer(split[i])
            
        return split
        
    def __str__(self, *args, **kwargs):
        data = 'There are '+str(len(self.zones))+' zone in zoneDealer'
        return data
    