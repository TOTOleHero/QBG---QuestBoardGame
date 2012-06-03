from log4py import Logger

class Parser(object):
	
	log = None
	
	fileName = None
	
	def __init__(self,fileName):
		self.log = Logger().get_instance(self.__class__.__name__)
		self.log.debug('Init parser for file '+fileName)
		self.fileName = fileName
		
		
	def loadInClass(self,className):
		pass