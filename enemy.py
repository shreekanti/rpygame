from random import randint
from character import Character
class Enemy(Character):
  def __init__(self, player):
    Character.__init__(self)
    self.name = 'a Devil Dragon'
    self.health = randint(1, player.health)
 
