import os
class Levelgen:
    def __init__(self,size):
        self.size=size
        if self.size <2:
            raise Exception("Hiba! A pálya mérete túl kicsi!")
        elif self.size > 20:
            raise Exception("Hiba! A pálya mérete túl nagy!")
    def Generate(self):
        os.system('cls')
        r=0
        c=0
        rl=[]
        sup=0
        self.level=[]
        while r!=self.size:
            sup+=self.size
            while c!=sup:
                if c<9:
                    rl.append(" {} |".format(c+1))
                elif c<99:
                    rl.append(" {}|".format(c+1))
                else:
                    rl.append("{}|".format(c+1))
                c+=1
            row="|"
            for x in rl:
                row="{}{}".format(row,x)
            rl.clear()
            self.level.append(row)
            r+=1
        return self.level