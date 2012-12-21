from log4py import Logger

class RoomDealer:
    
    def __init__(self,rooms = []):
        self.log = Logger().get_instance(self.__class__.__name__)
        self.rooms = rooms
    
    def addRoom(self,room):
        self.log.debug('Add room '+room.name)
        self.rooms.append(room)
    
    def getAndRemoveRoom(self):
        if len(self.rooms) > 0:
            room = self.rooms.pop()
            room.roomDealer = self
            return room
    
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
            for room in self.rooms:
                split[index].append(room)
                index = index + 1
                if index == count:
                    index=0
            
            for i in range(0,count):
                split[i] = RoomDealer(split[i])
            
        return split
        
    def __str__(self, *args, **kwargs):
        data = 'There are '+str(len(self.rooms))+' room in roomDealer'
        return data
    