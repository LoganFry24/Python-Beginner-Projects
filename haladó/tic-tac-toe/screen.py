#graphics of the game
from system import System
class Screen:
    def __init__(self,level,player1):
        self.level=level
        self.player1=player1
    def Convert(self,lepes):
        if lepes <10:
            lepes =" {} ".format(str(lepes))
        elif lepes <100:
            lepes =" {}".format(str(lepes))
        else:
            lepes="{}".format(str(lepes))
        return lepes
    def Update(self,lepesek,turn):
        i=0
        lepesek=self.Convert(lepesek)
        while i!=len(self.level):
            x=0
            while x!=len(self.level[i]):
                if x<len(self.level[i])-2: #2.modszer
                    sor = "{}{}{}".format(self.level[i][x],self.level[i][x+1],self.level[i][x+2])
                    if sor ==lepesek:
                        if turn==self.player1:
                            self.level[i][x]=' '
                            self.level[i][x+1]='X'
                            self.level[i][x+2]=' '
                        else:
                            self.level[i][x]=' '
                            self.level[i][x+1]='O'
                            self.level[i][x+2]=' '
                x+=1
            i+=1
        return self.level
    def Render(self,turn,msg):
        sc=System()
        del sc
        y=0
        while y != len(self.level):
            x=0
            sor=""
            while x!=len(self.level[y]):
                sor="{}{}".format(sor,self.level[y][x])
                x+=1
            print(sor)
            y+=1
        print("{} köre jön!".format(turn))
        print("Adja meg a hely számát!")
        print(msg)