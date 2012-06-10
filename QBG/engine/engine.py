class Engine(object):
    
    
    
    def __init__(self):
        self.loaders = []    
        self.data = {}
        self.donjonSubTypeCount = {}

    
    def run(self):
        
        for loader in self.loaders:
            loader.load(self.data)
            print loader.__class__.__name__ + ' Finished'
        print 'Run loaders Finished'
    
    
    def authorizeDonjonSubTypeCount(self,subType, count):
        if subType in self.data['floor']:
            self.donjonSubTypeCount[subType] = count
        
    def addLoader(self,loader):
        self.loaders.append(loader)