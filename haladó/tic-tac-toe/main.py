#the game loop
from control import Controls
from screen import Screen
from judge import Judge
class Main:
    def __init__(self,mode,player1,player2,difficulty,level,size,r):
        self.mode=mode
        self.player1=player1
        self.player2=player2
        self.difficulty=difficulty
        self.level=level
        self.size=size
        self.round=r
    def Game(self):
        #variables
        loop=True
        msg=""
        lepesek=[]
        turn =self.player1
        end=False
        #constructors
        control=Controls(self.mode,self.size,self.difficulty)
        graph=Screen(self.level,self.player1)
        judge=Judge(self.level,self.size,self.player1,self.player2)
        #the game loop
        while loop==True:
            #Render
            graph.Render(turn,msg)
            # get the input from a player or a bot
            msg=control.Input(turn,lepesek)
            #Update the level
            graph.Update(lepesek[-1],turn)
            #Condition
            end =judge.Check()
            if end !=False:
                msg = "Vége a {}.körnek! A győztes: {}".format(self.round,end)
                graph.Render(turn,msg)
                input("A tovább lépéshez nyomj entert!")
                break
            elif len(lepesek) == self.size**2:
                msg = "Vége a körnek! Döntetlen!"
                graph.Render(turn,msg)
                input("A tovább lépéshez nyomj entert!")
                break
            #switch the players
            elif msg=="":
                if turn == self.player1:
                    turn=self.player2
                else:
                    turn=self.player1
        del control
        del graph
        del judge
        return end   