from system import System
class Levelgen:
    def __init__(self,size):
        self.size=size
        if self.size <2:
            raise Exception("Hiba! A pálya mérete túl kicsi!")
        elif self.size > 20:
            raise Exception("Hiba! A pálya mérete túl nagy!")
    def Generate(self):
        sc=System()
        del sc
        width=self.size*4+1
        self.level=[['|' for x in range(width)]for y in range(self.size)]
        y=0
        c=1
        while y!=self.size:
            self.level[y][0]=='|'
            x=1
            while x!=width:
                if c<=9:
                    self.level[y][x]=' '
                    self.level[y][x+1]=c
                    self.level[y][x+2]=' '
                    self.level[y][x+3]='|'
                elif c<=99:
                    self.level[y][x]=' '
                    self.level[y][x+1]=str(c)[0]
                    self.level[y][x+2]=str(c)[1]
                    self.level[y][x+3]='|'
                else:
                    self.level[y][x]=str(c)[0]
                    self.level[y][x+1]=str(c)[1]
                    self.level[y][x+2]=str(c)[2]
                    self.level[y][x+3]='|'
                c+=1
                x+=4
            y+=1
        return self.level