#starting point of the game
import os
from controller import Controller
#main class
class Program:
    #Constants
    def __init__(self,WIDTH,HEIGHT,LINEWIDTH,bgcolor,linecolor,CIRCLE_COLOR,CROSS_COLOR):
        self.WIDTH=WIDTH
        self.HEIGHT=HEIGHT
        self.LINEWIDTH=LINEWIDTH
        self.bgcolor=bgcolor
        self.linecolor=linecolor
        self.CIRCLE_COLOR=CIRCLE_COLOR
        self.CROSS_COLOR=CROSS_COLOR
    def Start(self):
        os.system("cls")
        #terminal test
        print("The game is running!")
        controller=Controller(self.WIDTH,self.HEIGHT,self.bgcolor,self.linecolor,self.LINEWIDTH,self.CIRCLE_COLOR,self.CROSS_COLOR)
        controller.Start()
# ---------
# CONSTANTS
# ---------
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15

BG_COLOR = (20,189,172)
LINE_COLOR = (13,161,146)
CIRCLE_COLOR = (242, 235, 211)
CROSS_COLOR = (84, 84, 84)

if __name__ == '__main__':
    game= Program(WIDTH,HEIGHT,LINE_WIDTH,BG_COLOR,LINE_COLOR,CIRCLE_COLOR,CROSS_COLOR)
    game.Start()
