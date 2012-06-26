from log4py import Logger

class Direction(object):

    SOUTH = 'south'
    
    NORTH = 'north'

    EAST = 'east'
    
    WEST = 'west'

    directionCompatibility = {'north':'south', 'south':'north', 'east':'west', 'west':'east'}
    
