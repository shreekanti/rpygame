from random import randint
from character import Character
from enemy import Enemy
#from commands import Com
class Player(Character):
  def __init__(self):
    Character.__init__(self)
    self.state = 'normal'
    self.health = 10
    self.health_max = 10
    self.wealth=15
    self.wealth_max=15
    self.Commands ={
  'quit': Player.quit,
  'help': Player.help,
  'status':Player.status,
  'rest': Player.rest,
  'explore':Player.explore,
  'flee': Player.flee,
  'attack': Player.attack,
  }
  def quit(self):
    print ("%s can't find the way back home, and dies of starvation.\nR.I.P." % self.name)
    self.health = 0
  def help(self): print (self.Commands.keys())
  def status(self):
    print ("%s's health: %d/%d" % (self.name, self.health, self.health_max))
    print ("%s's wealth: %d/%d" % (self.name, self.wealth, self.wealth_max))
  def tired(self):
    print ("%s feels tired." % self.name)
    self.health = max(1, self.health - 1)
  def rest(self):
    if self.state != 'normal': print( "%s can't rest now!" % self.name); self.enemy_attacks()
    else:
      print( "%s rests." % self.name)
      if randint(0, 1):
        self.enemy = Enemy(self)
        print ("%s is rudely awakened by %s!" % (self.name, self.enemy.name))
        self.state = 'fight'
        self.enemy_attacks()
      else:
        if self.health < self.health_max:
          self.health = self.health + 1
        else: print ("%s slept too much." % self.name); self.health = self.health - 1
  def explore(self):
    if self.state != 'normal':
      print ("%s is too busy right now!" % self.name)
      self.enemy_attacks()
    else:
      print ("%s explores a twisty passage." % self.name)
      if randint(0, 1):
        self.enemy = Enemy(self)
        print( "%s encounters %s!" % (self.name, self.enemy.name))
        self.state = 'fight'
      else:
        if randint(0, 1): self.tired()
  def flee(self):
    if self.state != 'fight': print ("%s runs in circles for a while." % self.name); self.tired()
    else:
      if randint(1, self.health + 5) > randint(1, self.enemy.health):
        print ("%s flees from %s." % (self.name, self.enemy.name))
        self.enemy = None
        self.state = 'normal'
      else: print ("%s couldn't escape from %s!" % (self.name, self.enemy.name)); self.enemy_attacks()
  def attack(self):
    if self.state != 'fight': print ("%s swats the air, without notable results." % self.name); self.tired()
    else:
      if self.do_damage(self.enemy):
        print ("%s killed %s!" % (self.name, self.enemy.name))
        self.wealth=self.wealth+self.enemy.wealth
        print("%s takes wealth %s from %s"%(self.name,self.wealth,self.enemy.name))
        self.enemy = None
        self.state = 'normal'
        if randint(0, self.health) < 10:
          self.health = self.health + 1
          self.health_max = self.health_max + 1
          print ("%s feels stronger !" % self.name)
      else: self.enemy_attacks()
  def enemy_attacks(self):
    if self.enemy.do_damage(self):
      #=self.enemy.n
      print( "%s was slaughtered by %s!!!\nR.I.P." %(self.name, self.enemy.name))
    
  """Commands ={
  'quit': Player.quit,
  'help': Player.help,
  'status': Player.status,
  'rest': Player.rest,
  'explore': Player.explore,
  'flee': Player.flee,
  'attack': Player.attack,
  }"""
 
"""p = Player()
p.name = input("What is your character's name? ")
print ("(type help to get a list of actions which u can do)\n")
print( "%s enters a dark cave, searching for adventure." % p.name)
 
while(p.health > 0):
  line = input("> ")
  args = line.split()
  if len(args) > 0:
    commandFound = False
    for c in Commands.keys():
      if args[0] == c[:len(args[0])]:
        Commands[c](p)
        commandFound = True
        break
    if not commandFound:
      print ("%s doesn't understand the suggestion." % p.name)"""
 
