from random import randint
from character import Character
from enemy import Enemy
from player import Player


p = Player()
Commands=p.Commands
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
      print ("%s doesn't understand the suggestion." % p.name)
"""if __name__=="__main__"
  "" print("mAIN")"""
    
