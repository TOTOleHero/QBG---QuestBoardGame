# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="thomas"
__date__ ="$7 juin 2013 08:34:16$"

class Player:
    
    def __init__(self):
        self.firstname = ''
        self.lastname = ''
        self.characters = []
        self.uuid = ''
        
    def addCharacter(self,character):
        self.characters.append(character)
        
    def removeCharacter(self,character):
        pass
    
    
        
        

if __name__ == "__main__":
    print "Hello World"
