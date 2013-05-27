#! /usr/bin/env python

from engine.engine import Engine
from engine.loaders.roomloader import RoomLoader
from engine.loaders.tileloader import TileLoader
from engine.loaders.itemloader import ItemLoader
from engine.loaders.creatureloader import CreatureLoader
from engine.loaders.tilefunctionloader import TileFunctionLoader
from engine.renders.asciirender import AsciiRender
from engine.tabletop import TileException
import copy
import os

from log4py import Logger




filePath = os.path.dirname(__file__)
rootPath = os.path.realpath(filePath+os.sep+'..')

Logger.configfiles.append(rootPath+os.sep+'conf'+os.sep+'log4py.conf')

e = Engine()

tileLoader              = TileLoader(rootPath+os.sep+'data'+os.sep+'tiles')
tileFunctionLoader      = TileFunctionLoader(rootPath+os.sep+'data'+os.sep+'tilesfunction')
roomLoader              = RoomLoader(rootPath+os.sep+'data'+os.sep+'rooms',tileFunctionLoader)
itemLoader              = ItemLoader(rootPath+os.sep+'data'+os.sep+'items')
creatureLoader          = CreatureLoader(rootPath+os.sep+'data'+os.sep+'creatures',itemLoader)

e.addLoader(itemLoader)
e.addLoader(creatureLoader)

e.addLoader(tileLoader)
e.addLoader(tileFunctionLoader)
e.addLoader(roomLoader)



e.load()
for rooms in e.data['room'].itervalues():
    index=0
    for room in rooms:
        print 'check '+str(index)+':'+room.name
        room.checkGridSizes()
        index += 1
        
e.authorizeDungeonSubTypeCount('corridor',12)
e.authorizeDungeonSubTypeCount('dungeon-room',4)
e.authorizeDungeonSubTypeCount('objective-room',1)

e.generateDongeon()
#===============================================================================
# e.generateDongeonArray.append(copy.deepcopy(e.data['room']['corridor'][1]))
# e.generateDongeonArray.append(copy.deepcopy(e.data['room']['corridor'][1]))
# e.generateDongeonArray.append(copy.deepcopy(e.data['room']['corridor'][0]))
# e.generateDongeonArray.append(copy.deepcopy(e.data['room']['dungeon-room'][0]))
# e.generateDongeonArray.append(copy.deepcopy(e.data['room']['corridor'][1]))
#===============================================================================



try:
    e.setRender(AsciiRender())
except engine.tabletop.TileException :
    Print('no render')


    
    pass

e.render()



