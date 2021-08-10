#the game loop
from control import Controls
from screen import Screen
from judge import Judge
class Main:
    def __init__(self,mode,names,level,size):
        self.mode=mode
        self.size=size
        self.level=level
        self.player1=names[0]
        self.difficulty=0
        if mode == "S":
            self.difficulty=names[1]
            self.player2="Computer"
        elif mode=="M":
            self.player2=names[1]
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
                msg = "Vége a játéknak! A győztes: {}".format(end)
                graph.Render(turn,msg)
                break
            elif len(lepesek) == self.size**2:
                msg = "Vége a játéknak! Nincs több hely!"
                graph.Render(turn,msg)
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
            
            