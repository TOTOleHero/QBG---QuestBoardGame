#! /usr/bin/env python

from engine.engine import Engine
from engine.loaders.floorloader import FloorLoader
from engine.loaders.tileloader import TileLoader
from engine.loaders.tilefunctionloader import TileFunctionLoader

from log4py import Logger

Logger.configfiles.append('conf/log4py.conf')

e = Engine()

tileLoader          = TileLoader('data/tiles')
tileFunctionLoader  = TileFunctionLoader('data/tilesfunction')
floorLoader         = FloorLoader('data/floors',tileFunctionLoader)

e.addLoader(tileLoader)
e.addLoader(tileFunctionLoader)
e.addLoader(floorLoader)


e.run()
for floors in e.data['floor'].itervalues():
    for floor in floors:
        print 'check '+floor.name
        floor.checkFloorSizes()
        
e.authorizeDonjonSubTypeCount('corridor',12)
e.authorizeDonjonSubTypeCount('dungeon-room',2)
e.authorizeDonjonSubTypeCount('objective-room',1)





