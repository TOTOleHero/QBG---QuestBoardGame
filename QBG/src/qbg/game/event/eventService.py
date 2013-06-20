# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="Thomas Lecarpentier / TOTOleHero <thomas.lecarpentier+coder[at]gmail.com>"
__date__ ="$20 juin 2013 09:01:22$"


class EventHandlerContainer(object):
    
    def __init__(self,event):
        self.event = event
        self.eventHandler = []
        
    def addHandler(self,eventHandler):
        self.eventHandler.append(eventHandler)


class EventService(object):
    
    def __init__(self):
        self.eventHandlers = {}
    
    def registerEvent(self,eventHandler, event):
        pass
        
    


if __name__ == "__main__":
    print "Hello World"
