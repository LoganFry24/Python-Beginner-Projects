#gamemode class
# here we can choose between pvp and pve
import os
from validate import Validate
class Gamemode:
    def __init__(self,mode):
        self.mode=mode
    def Mode(self):
        if self.mode=="M":
            multi=Multiplayer()
            a=multi.Name()
            del multi
            return a
        elif self.mode=="S":
            single=Singleplayer()
            a=single.Name()
            del single
            return a
        else:
            raise Exception("Hibás paraméter a játékmód megadásánál!")
#multiplayer (pvp)
class Multiplayer:
    def Name(self):
        cons=Validate("Kérem az első játékos nevét!")
        self.player1=cons.check()
        del cons
        cons=Validate("Kérem a második játékos nevét!")
        self.player2=cons.check()
        del cons
        return self.player1,self.player2
#singleplayer (pve)
class Singleplayer:
    def Name(self):
        cons=Validate("Kérem a játékos nevét!")
        self.player=cons.check()
        del cons
        cons=Validate("Kérem a nehézségi szint számát!")
        self.difficulty=cons.check()
        del cons
        return self.player, self.difficulty