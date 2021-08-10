class Bot:
    def __init__(self,size,lepesek,difficulty):
        self.size=size
        self.lepesek=lepesek
        self.difficulty=difficulty
    def GetInput(self):
        msg=""
        #easy
        if self.difficulty==1:
            from easy import Easy
            con = Easy(self.size,self.lepesek)
            msg= con.Step()
            del con
        # normal
        elif self.difficulty==2:
            from normal import Normal
            con = Normal(self.size,self.lepesek)
            msg= con.Step()
            del con
        # hard
        elif self.difficulty==3:
            from hard import Hard
            con = Hard(self.size,self.lepesek)
            msg= con.Step()
            del con
        # error
        else:
            raise Exception("Hibás nehézségi szint!")
        return msg