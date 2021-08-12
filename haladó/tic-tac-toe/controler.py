#menu system
from interface import Interface #GUI of the menu
from gamemode import Gamemode
from levelgenerator import Levelgen
from main import Main #the gameloop
class Controler:
    def CreateGame(self):
        #invite the interface of the menu
        interface=Interface()
        #get the names and the gamemode
        self.mode=interface.SelectMode()
        players=Gamemode(self.mode)
        names=players.Mode()
        del players
        self.player1=names[0]
        self.difficulty=0
        if self.mode == "S":
            self.difficulty=names[1]
            self.player2="Computer"
        elif self.mode=="M":
            self.player2=names[1]
        else:
            raise Exception("Hibás paraméter a játékmód megadásánál!")
        #get the size of the map
        self.size=interface.SelectSize()
        #get the number of the rounds
        rounds=interface.SelectRounds()
        # start the game
        self.round=0
        p1=0
        p2=0
        while self.round!= rounds:
            winner=self.CreateRound()
            if winner == self.player1:
                p1+=1
            elif winner == self.player2:
                p2+=1
            interface.Statement(self.round+1,p1,p2,self.player1,self.player2)
            self.round+=1
        #the game's result
        interface.Result(p1,p2,self.player1,self.player2)
        del interface
    def CreateRound(self):
        #generate the map
        l=Levelgen(self.size)
        self.level=l.Generate()
        del l
        #let's create a game with the user's parameters
        game=Main(self.mode,self.player1,self.player2,self.difficulty,self.level,self.size,self.round+1)
        winner=game.Game() #the function of the gameloop
        del game
        return winner
    
con=Controler()
con.CreateGame()
input("system.pause")