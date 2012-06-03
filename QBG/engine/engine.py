class Engine(object):
    
    loaders = []    
    
    def __init__(self,):
        pass
    
    def run(self):
        
        for loader in self.loaders:
            loader.load()
        print 'OK'
        
    def addLoader(self,loader):
        self.loaders.append(loader)