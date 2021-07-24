#graphics of the game
import os
class Screen:
    def __init__(self,level,player1,size):
        self.level=level
        self.player1=player1
        self.size=size
    def Update(self,lepesek,turn):
        i=0
        while i!=len(self.level):
            x=0
            while x!=len(self.level[i]):
                if self.level[i][x]==str(lepesek[-1]):
                    if turn==self.player1:
                        self.level[i].replace(str(lepesek[-1]),"X")  
                    else:
                        self.level[i].replace(str(lepesek[-1]),"O")  
                x+=1
            i+=1
    def Render(self,turn,msg):
        os.system('cls')
        print("{} köre jön!".format(turn))
        print("Adja meg a hely számát!")
        for x in self.level:
            print(x)
        print(msg)