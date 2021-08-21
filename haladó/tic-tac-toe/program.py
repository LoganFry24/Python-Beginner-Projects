# the new temporary starting point is the controler file
#the starting point of the program, to start the game you have to execute this file at first
#import classes
from gamemode import Gamemode
from levelgenerator import Levelgen
from main import Main
mode ="S"
size=3
r="teszt"
d=1
#constructors
players=Gamemode(mode) #gamemode
l=Levelgen(size)
#start the game with the methods
names=players.Mode() #get the names
level=l.Generate() #generate a map
game=Main(mode,names[0],names[1],d,level,size,r)
game.Game()
input("system.pause")