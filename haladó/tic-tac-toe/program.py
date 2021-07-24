#the starting point of the program, to start the game you have to execute this file at first
#import classes
from gamemode import Gamemode
from levelgenerator import Levelgen
from main import Main
mode ="S"
size=20
#constructors
players=Gamemode(mode) #gamemode
l=Levelgen(size)
#start the game with the methods
names=players.Mode() #get the names
level=l.Generate() #generate a map
game=Main(mode,names,level,size)
game.Game()
input("system.pause")