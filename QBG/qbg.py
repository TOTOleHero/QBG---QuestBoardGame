#! /usr/bin/env python

from engine.engine import Engine
from engine.loaders.floorloader import FloorLoader
from log4py import Logger

Logger.configfiles.append('conf/log4py.conf')

e = Engine()
e.addLoader(FloorLoader('data/floors'))

e.run()
