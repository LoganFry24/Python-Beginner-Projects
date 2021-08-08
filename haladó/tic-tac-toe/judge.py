#check the status of the game
from screen import Screen
class Judge(Screen):
    def __init__(self, level,size,player1,player2):
        self.level=level
        self.size=size
        self.player1=player1
        self.player2=player2
    def Check(self):
        end = self.Horizontal()
        if end ==False:
            end = self.Vertical()
            if end ==False:
                end =self.Transversal()
        return end
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
                    end = self.player1
                    break
                if p2 == self.size:
                    end = self.player2
                    break
                x+=1
            if end != False:
                break
            y+=1
        return end
    def Vertical(self):
        end =False
        x=0
        while x!= len(self.level[0]):
            y=0
            p1=0
            p2=0
            while y != self.size:
                if self.level[y][x] == 'X':
                    p1+=1
                if self.level[y][x] == 'O':
                    p2+=1
                if p1 == self.size:
                    end = self.player1
                    break
                if p2 == self.size:
                    end = self.player2
                    break
                y+=1
            if end != False:
                break
            x+=1
        return end
    def Transversal(self):
        end = False
        p1=0
        p2=0
        y=0
        x=2
        # from left to right
        while y != self.size:
            if self.level[y][x]== 'X':
                p1+=1
            if self.level[y][x]== 'O':
                p2+=1
            x+=4
            y+=1
        if p1 == self.size:
            end = self.player1
        elif p2 == self.size:
            end = self.player2
        else: #from right to left
            p1=0
            p2=0
            y=0
            x=len(self.level[0])-3
            while y != self.size:
                if self.level[y][x]== 'X':
                    p1+=1
                if self.level[y][x]== 'O':
                    p2+=1
                x-=4
                y+=1
            if p1 == self.size:
                end = self.player1
            elif p2 == self.size:
                end = self.player2      
        return end