# This class is copied from project http://code.google.com/p/pyquest/
from log4py import Logger

__author__="Justin Neddo <jtneddo[at]gmail.com>"
__date__ ="$20 mai 2013 11:04:44$"

class Character(object):
  '''
  classdocs
  '''

  
  TYPE_HERO = "hero"
  TYPE_MONSTER = "monster"



  
  #def __init__(self, name, type,move=0, weapon_skill=0, ballistic_skill=0,strength=0,toughness=0,wounds=0,initiative=0,attacks=0,gold=0,armor=0,damage=0):
  def __init__(self,itemsLoader):
    '''
    Constructor
    '''
    
    '''
    Logger
    '''
    self.log = Logger().get_instance(self.__class__.__name__)
    
    '''
    Tile loader able to convert tile CODE
    '''
    self.itemsLoader = itemsLoader
    
    
#    self._name = name
#    self._type = type
#    
#    self._move = move
#    self._weapon_skill = weapon_skill
#    self._ballistic_skill = ballistic_skill
#    self._strength = strength
#    self._toughness = toughness
#    self._wounds = wounds
#    self._current_wounds = wounds
#    self._initiative = initiative
#    self._attacks = attacks
#    self._gold = gold
#    self._armor = armor
#    self._damage = damage

    self._type = ""
    self._name = "" 
    """
    all Stats
    """
    
    self._move = 0
    self._weapon_skill = 0
    self._ballistic_skill = 0
    self._strength = 0
    self._toughness = 0
    self._wounds = 0
    self._initiative = 0
    self._attacks = 0
    self._gold = 0
    self._armor = 0
    self._damage = 0
    self._extra_damage = 0
    self._extra_damage_hit = 0
    self._pinning = 6
    self._current_wounds = 0
    
    # Default battle level is 1
    self._battle_level = 1
    
    
    self._effects = []


  
  def setDict(self,dictData):
    self.log.debug(str(dictData))
    self._name = dictData['name']
    self._type = dictData['type']
    self._weapon_skill = dictData['weaponSkill']
    self._ballistic_skill = dictData['ballisticSkill']
    self._strength = dictData['strength']
    self._wounds = dictData['wounds']
    self._initiative = dictData['initiative']
    self._attacks = dictData['attacks']

          
          
  def melee_hit_roll(self, target):
    attackroll = random.randint(1,6)
    
    # if the hit roll is a 6, we're done
    if attackroll == 6:
      return attackroll    
    
    hit_modifier = 0
    for e in self._effects:
      hit_modifier += e.hit_modifier(self, target)
    
    attackroll += hit_modifier
    
    if attackroll > 6:
      attackroll = 6
    elif attackroll < 1:
      attackroll = 1
    return attackroll
  
  def ranged_hit_roll(self, target):
    attackroll = random.randint(1,6)
    
    hit_modifier = 0
    for e in self._effects:
      hit_modifier += e.hit_modifier
    
    if attackroll > 6:
      attackroll = 6
    elif attackroll < 1:
      attackroll = 1
    return attackroll
  
  def is_hit(self, target, attackroll):
    if (attackroll == 1):
      return False
    if (attackroll == 6):
      return True
    if (attackroll >= to_hit_table[self._weapon_skill][target._weapon_skill]):
      return True
    return False
  
  def is_ranged_hit(self, target, attackroll):
    if (attackroll == 1):
      return False
    if (attackroll == 6):
      return True
    if attackroll >= self._ballistic_skill:
      return True
    return False
  
  def damage_roll(self, attackroll=1):
    dmg = 0
    x = self._damage
    if self._extra_damage_hit:
      if attackroll > self._extra_damage_hit:
        x += self._extra_damage
    while x:
      x = x - 1
      dmg += random.randint(1,6)
      
    dmg += self._strength
    return dmg
  
  def take_damage(self, damage, ignore_armor=False, ignore_toughness=False):
    tempdmg = damage
    if not ignore_armor:
      tempdmg -= self._armor
    if not ignore_toughness:
      tempdmg -= self._toughness
    if tempdmg > 0:
      self._current_wounds -= tempdmg  
    
  def zero_wounds(self):
    if self._type == "Character":
      print("\t",self._name,"falls!")
    else:
      print("\t",self._name,"dies!")
      
  def melee_attack(self, target):
    attackroll = self.melee_hit_roll(target)
    hit = self.is_hit(target, attackroll)
    if hit:
      dmg = self.damage_roll(attackroll)
      target.take_damage(dmg)
      print ("\t",self._name,"hits", target._name, "for", dmg)
    else:
      print ("\t",self._name,"missed!")
      
  def ranged_attack(self, target):
    attackroll = self.ranged_hit_roll(target)
    hit = self.is_ranged_hit(target, attackroll)
    if hit:
      dmg = self.damage_roll(attackroll)
      target.take_damage(dmg)
      print ("\t",self._name,"hits", target._name, "for", dmg)
    else:
      print ("\t",self._name,"missed!")
      
  def addeffect(self, effect):
    effect.roll()
    self._effects.append(effect)
    print (self._name,"-",effect)
  '''
  Event handlers
  '''
  def place(self, target):
    if hasattr(self, "_ambush"):
      ambushroll = random.randint(1,6)
      if ambushroll >= self._ambush:
        self.melee_attack(target)
        
    if hasattr(self, "_magic_ambush"):
      ambushroll = random.randint(1,6)
      if ambushroll >= self._ambush:
        self.melee_attack(target)
  
  def place_partyeffects(self, party):
    if hasattr(self, "_fear"):
      for p in party:
        fear = effects.Fear(self._name, 5)
        p.addeffect(fear)
