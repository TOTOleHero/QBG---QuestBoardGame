# This class is copied from project http://code.google.com/p/pyquest/

__author__="Justin Neddo <jtneddo[at]gmail.com>"
__date__ ="$20 mai 2013 11:15:00$"
  
"""
Base effects class
"""
class Effect(object):
  '''
  classdocs
  '''
  _name = ""
    
  def __init__(self):
    pass
    
  def hit_modifier(self, attacker, target):
    return 0
  
  def roll(self):
    pass