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
        control=Controls(self.mode)
        graph=Screen(self.level,self.player1,self.size)
        loop=True
        turn =self.player1
        lepesek=[]
        graph.Render(turn,"")
        msg=""
        while loop==True:
            msg=control.Input(turn,self.size,lepesek)
            #print("kép")
            #Update
            graph.Update(lepesek,turn)
            #Condition
            #Render
            #graph.Render(turn,msg)
            if turn == self.player1:
                turn=self.player2
            else:
                turn=self.player1