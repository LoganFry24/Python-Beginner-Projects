#the game loop
from control import Controls
from screen import Screen
class Main:
    def __init__(self,mode,names,level,size):
        self.mode=mode
        self.size=size
        self.level=level
        self.player1=names[0]
        if mode == "S":
            self.difficulty=names[1]
            self.player2="computer"
        elif mode=="M":
            self.player2=names[1]
    def Game(self):
        #variables
        loop=True
        msg=""
        lepesek=[]
        turn =self.player1
        #constructors
        control=Controls(self.mode)
        graph=Screen(self.level,self.player1)
        #the game loop
        while loop==True:
            #Render
            graph.Render(turn,msg)
            # get the input from a player or a bot
            msg=control.Input(turn,self.size,lepesek)
            #Update the level
            graph.Update(lepesek[-1],turn)
            #Condition
            if len(lepesek) == self.size**2:
                msg ="Vége a játéknak! Nincs több hely"
                graph.Render(turn,msg)
                break
            if msg=="":
                if turn == self.player1:
                    turn=self.player2
                else:
                    turn=self.player1
            
            