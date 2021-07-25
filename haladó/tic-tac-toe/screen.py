#graphics of the game
import os
class Screen:
    def __init__(self,level,player1,size):
        self.level=level
        self.player1=player1
        self.size=size
    def Update(self,lepesek,turn):
        width=len(self.level[0])
        track= [[0 for x in range(width)]for y in range(len(self.level))]
        i=0
        while i!=len(self.level):
            x=0
            while x!= width:
                track[i][x]=self.level[i][x]
                x+=1
            i+=1
    def Render(self,turn,msg):
        os.system('cls')
        print("{} köre jön!".format(turn))
        print("Adja meg a hely számát!")
        for x in self.level:
            print(x)
        print(msg)