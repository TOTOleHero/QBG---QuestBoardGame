#! /usr/bin/env python

from qbg.engine import Engine
from qbg.game.space.zoneloader import ZoneLoader
from qbg.game.space.tileloader import TileLoader
from qbg.items.itemloader import ItemLoader
from qbg.characters.characterloader import CharacterLoader
from qbg.game.space.tilefunctionloader import TileFunctionLoader
from qbg.renders.asciirender import AsciiRender
from qbg.game.space.tabletop import TileException
from qbg.game.event.eventloader import EventLoader

import copy
import os

from log4py import Logger




filePath = os.path.dirname(__file__)
rootPath = os.path.realpath(filePath+os.sep+'..')

Logger.configfiles.append(rootPath+os.sep+'conf'+os.sep+'log4py.conf')

e = Engine()

eventLoader             = EventLoader(rootPath+os.sep+'data'+os.sep+'events')
tileLoader              = TileLoader(rootPath+os.sep+'data'+os.sep+'tiles')
tileFunctionLoader      = TileFunctionLoader(rootPath+os.sep+'data'+os.sep+'tilesfunction')
zoneLoader              = ZoneLoader(rootPath+os.sep+'data'+os.sep+'zones',tileFunctionLoader)
itemLoader              = ItemLoader(rootPath+os.sep+'data'+os.sep+'items')
characterLoader          = CharacterLoader(rootPath+os.sep+'data'+os.sep+'characters',itemLoader)

e.addLoader(eventLoader)

e.addLoader(itemLoader)
e.addLoader(characterLoader)

e.addLoader(tileLoader)
e.addLoader(tileFunctionLoader)
e.addLoader(zoneLoader)



e.load()
for zones in e.data['zone'].itervalues():
    index=0
    for zone in zones:
        print 'check '+str(index)+':'+zone.name
        zone.checkGridSizes()
        index += 1
        
e.authorizeDungeonSubTypeCount('corridor',12)
e.authorizeDungeonSubTypeCount('dungeon-zone',4)
e.authorizeDungeonSubTypeCount('objective-zone',1)

e.generateDongeon()
#===============================================================================
# e.generateDongeonArray.append(copy.deepcopy(e.data['zone']['corridor'][1]))
# e.generateDongeonArray.append(copy.deepcopy(e.data['zone']['corridor'][1]))
# e.generateDongeonArray.append(copy.deepcopy(e.data['zone']['corridor'][0]))
# e.generateDongeonArray.append(copy.deepcopy(e.data['zone']['dungeon-zone'][0]))
# e.generateDongeonArray.append(copy.deepcopy(e.data['zone']['corridor'][1]))
#===============================================================================



try:
    e.setRender(AsciiRender())
except qbg.tabletop.TileException :
    Print('no render')


    
    pass

e.render()



