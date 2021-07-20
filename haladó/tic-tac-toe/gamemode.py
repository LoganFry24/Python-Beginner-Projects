#gamemode class
# here we can choose between pvp and pve
import os
class Gamemode:
    def __init__(self,mode):
        self.mode=mode
    def Mode(self):
        if self.mode=="M":
            multi=Multiplayer()
            l=multi.Name()
            print(l[0])
            print(l[1])
        elif self.mode=="S":
            single=Singleplayer()
        else:
            raise Exception("Hibás paraméter a játékmód megadásánál!")
#multiplayer (pvp)
class Multiplayer:
    def Name(self):
        os.system('cls')
        self.player1=input("Kérem az első játékos nevét!")
        os.system('cls')
        self.player2=input("Kérem a második játékos nevét!")
        return self.player1,self.player2
#singleplayer (pve)
class Singleplayer:
    def Name(self):
        os.system('cls')
        self.player=input("Kérem a játékos nevét!")
        os.system('cls')
        self.difficulty=int(input("Kérem a nehézségi szint számát!"))