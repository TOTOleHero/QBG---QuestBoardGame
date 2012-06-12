from render import Render

class AsciiRender(Render):
    pass

    def __init__(self):
        pass
    
    def renderTabletop(self,tableTop):
        asciiMap = ''
        for i in range(0,tableTop.globalWidth):
            for j in range(0,tableTop.globalHeight):
                asciiMap += 'O'
            asciiMap += '\n'
        print asciiMap
            
        pass