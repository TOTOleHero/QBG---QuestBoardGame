from log4py import Logger
from qbg.config.loaders.playerloader import PlayerLoader
from qbg.game.player.player import Player

__author__="Thomas Lecarpentier / TOTOleHero <thomas.lecarpentier+coder[at]gmail.com>"
__date__ ="$3 juin 2013 09:01:02$"

class PlayerManager:
    
    def __init__(self,playerLoader):
        self.playerLoader = playerLoader
        
    def createPlayer(self,firstname,lastname):
        player = Player()
        player.firstname = firstname
        player.lastname = lastname
        
        return player
    
    def dump(self,player):
        pass

if __name__ == "__main__":
    playerloader = PlayerLoader()
    
    playermanager = PlayerManager(playerloader)
    player = playermanager.createPlayer('John','Do')
    
    print 'hello '+ player.firstname + ' '+ player.lastname
    
    playermanager.dump(player)
    
    
