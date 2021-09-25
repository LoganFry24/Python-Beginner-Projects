class Model:
    def __init__(self):
        self.board=[[0 for x in range(3)]for y in range(3)]
        self.turn= 1
    def Update(self,row,col):
        #success
        if self.board[row][col]==0:
            self.board[row][col]=self.turn
            self.turn = self.turn % 2 + 1
        return self.board
    def Check(self):
        end = self.Horizontal()
        method=0
        if end ==False:
            end = self.Vertical()
            if end ==False:
                end=self.Adiagonal()
                if end ==False:
                    end=self.Ddiagonal()
                    if end !=False:
                        method="Ddiagonal"
                else:
                    method="Adiagonal"
            else:
                method="Vertical"
        else:
            method="Horizontal"
        return end,method
    def Horizontal(self):
        end =False
        y=0
        while y != len(self.board):
            x=0
            p1=0
            p2=0
            while x!=len(self.board[y]):
                if self.board[y][x] == 1:
                    p1+=1
                if self.board[y][x] == 2:
                    p2+=1
                if p1 == 3:
                    end = 1
                    break
                if p2 == 3:
                    end = 2
                    break
                x+=1
            if end != False:
                break
            y+=1
        return end
    def Vertical(self):
        end =False
        x=0
        while x!= len(self.board[0]):
            y=0
            p1=0
            p2=0
            while y != 3:
                if self.board[y][x] == 1:
                    p1+=1
                if self.board[y][x] == 2:
                    p2+=1
                if p1 == 3:
                    end = 1
                    break
                if p2 == 3:
                    end = 2
                    break
                y+=1
            if end != False:
                break
            x+=1
        return end
    def Adiagonal(self):
        end = False
        if self.board[2][0] == 1 and self.board[1][1] == 1 and self.board[0][2] == 1:
            end=1
        if self.board[2][0] == 2 and self.board[1][1] == 2 and self.board[0][2] == 2:
            end=2
        return end
    def Ddiagonal(self):
        end = False
        if self.board[0][0] == 1 and self.board[1][1] == 1 and self.board[2][2] == 1:
            end=1
        if self.board[0][0] == 2 and self.board[1][1] == 2 and self.board[2][2] == 2:
            end=2
        return end