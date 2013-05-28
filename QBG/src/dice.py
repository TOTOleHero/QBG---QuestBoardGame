# Module for generating random numbers in a dice-like fashion
# Authors: Joey Sabey, GameFreak7744@gmail.com
# Initial code in D, adapted by Thomas Lecarpentier
# Copyright: @ Joey Sabey 2012
# License: MIT License


import random

'''
  Represents a single n-sided dice
  Example:
  ---
  Dice d8 = new Dice(8);
  d8.roll();
  writeln(d8.result); //prints a random number between 1 and 8
  writeln(d8.result); //prints the same number
  writeln(d8.roll()); //prints a new random number between 1 and 8
 
'''
class Dice :
      
  def __init__(self,sides = 6) :    
    # by default dice have 6 sides
    self._sides = self.checkSides(sides)
    self._result = 0
      
  '''
  Returns: Current number of sides of the dice
  '''
  def getSides(self):
    return self._sides
        

  '''
  Allows you to set the the number of sides of the dice, to anything from 2 to ubyte.max
  '''
  def setSides(self,sides):
    self._sides = self.checkSides(sides)
    return self._sides

  '''
    Returns: Result of the last roll of the dice
  '''
  def getResult(self):
    return self.checkResult()
        
        
  '''
  Returns: A random number from 1 to sides
  '''
  def roll(self):
    self._result = random.randint(1, self._sides)
    return self._result
        
        
  def checkSides(self,sides):
    if sides < 2 :
      raise Error('Dice must have at least 2 sides, passed ' + sides )
    return sides
        
        
  def checkResult():
    if self._result == 0:
      raise Error("Dice has not been rolled yet; must call roll() first")
    return self._result
        
if __name__ == "__main__":
        
	dice = Dice()
	print dice.roll()



