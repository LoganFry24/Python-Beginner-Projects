#we have to recognise the type of the control
class Controls:
    def __init__(self,mode,size,difficulty):
        self.mode=mode
        self.size=size
        self.difficulty=difficulty
    def Input(self,turn,lepesek):
        if self.mode =="S" and turn=="Computer":
            from bot import Bot
            con=Bot(self.size,lepesek,self.difficulty)
            msg=con.GetInput()
            del con
            return msg
        else:
            from human import Human
            con=Human(self.size,lepesek)
            msg = con.GetInput()
            del con
            return msg