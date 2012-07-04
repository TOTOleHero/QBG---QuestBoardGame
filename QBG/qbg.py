#! /usr/bin/env python

from engine.engine import Engine
from engine.loaders.roomloader import RoomLoader
from engine.loaders.tileloader import TileLoader
from engine.loaders.tilefunctionloader import TileFunctionLoader
from engine.renders.asciirender import AsciiRender
import copy

from log4py import Logger

Logger.configfiles.append('conf/log4py.conf')

e = Engine()

tileLoader          = TileLoader('data/tiles')
tileFunctionLoader  = TileFunctionLoader('data/tilesfunction')
roomLoader         = RoomLoader('data/rooms',tileFunctionLoader)

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

print('###'+str(len(e.data['room']['corridor'][0].tiles))+'##')

#e.generateDongeon()
e.generateDongeonArray.append(copy.deepcopy(e.data['room']['corridor'][1]))
e.generateDongeonArray.append(copy.deepcopy(e.data['room']['corridor'][1]))
e.generateDongeonArray.append(copy.deepcopy(e.data['room']['corridor'][0]))
e.generateDongeonArray.append(copy.deepcopy(e.data['room']['dungeon-room'][0]))

print(e.generateDongeonArray)

e.setRender(AsciiRender())

e.render()



