#we have to recognise the type of the control
class Controls:
    def __init__(self,mode):
        self.mode=mode
    def Input(self,turn,size,lepesek):
        if self.mode =="S" and turn=="computer":
            msg=self.Bot(size)
            from bot import Bot
            con=Bot(size,lepesek)
            return msg
        else:
            from human import Human
            con=Human(size,lepesek)
            msg = con.GetInput(size,lepesek)
            return msg