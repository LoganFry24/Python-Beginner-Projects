#check the status of the game
from screen import Screen
class Judge(Screen):
    def __init__(self, level,size):
        self.level=level
        self.size=size
    def Check(self):
        pass
    def Horizontal(self):
        end =False
        y=0
        while y != len(self.level):
            x=0
            p1=0
            p2=0
            while x!=len(self.level[y]):
                if self.level[y][x] == 'X':
                    p1+=1
                if self.level[y][x] == 'O':
                    p2+=1
                if p1 == self.size:
                    end = 1
                    break
                if p2 == self.size:
                    end == 2
                    break
                x+=1
            else:
                continue
            y+=1
            break
        return end
    def Vertical(self):
        pass
    def Transversal(self):
        pass
i=0
while i!=2:
    print("sor")
    e=0
    for x in range(0 , 8):
        print("e")
        if x == 2:
            break
    else:
        continue
    i+=1
    break