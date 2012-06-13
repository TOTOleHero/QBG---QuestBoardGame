#! /usr/bin/env python

from engine.engine import Engine
from engine.loaders.floorloader import FloorLoader
from engine.loaders.tileloader import TileLoader
from engine.loaders.tilefunctionloader import TileFunctionLoader
from engine.renders.asciirender import AsciiRender
import copy

from log4py import Logger

Logger.configfiles.append('conf/log4py.conf')

e = Engine()

tileLoader          = TileLoader('data/tiles')
tileFunctionLoader  = TileFunctionLoader('data/tilesfunction')
floorLoader         = FloorLoader('data/floors',tileFunctionLoader)

e.addLoader(tileLoader)
e.addLoader(tileFunctionLoader)
e.addLoader(floorLoader)


e.load()
for floors in e.data['floor'].itervalues():
    index=0
    for floor in floors:
        print 'check '+str(index)+':'+floor.name
        floor.checkFloorSizes()
        index += 1
        
e.authorizeDungeonSubTypeCount('corridor',12)
e.authorizeDungeonSubTypeCount('dungeon-room',4)
e.authorizeDungeonSubTypeCount('objective-room',1)

#e.generateDongeon()
e.generateDongeonArray.append(copy.deepcopy(e.data['floor']['corridor'][0]))
e.generateDongeonArray.append(copy.deepcopy(e.data['floor']['corridor'][0]))
e.generateDongeonArray.append(copy.deepcopy(e.data['floor']['corridor'][1]))
e.generateDongeonArray.append(copy.deepcopy(e.data['floor']['dungeon-room'][0]))

print(e.generateDongeonArray)

e.setRender(AsciiRender())

e.render()



