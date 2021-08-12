#the interface of the menu
from system import System
class Interface:
    def SelectMode(self):
        correct=False
        msg=""
        while correct!=True:
            print("Amőba játék (Tic-Tac-Toe game)")
            print()
            print("Főmenü")
            print()
            print("Egyjátékos mód 1-es gomb")
            print()
            print("Többjátékos mód 2-es gomb")
            print(msg)
            key=input("Válasz egy játékmódót!")
            sc =System()
            del sc
            if key =='1' or key == '2':
                if key=='1':
                    key='S'
                else:
                    key='M'
                correct=True
            else:
                msg="Ilyen játék mód nincs! Adj meg egy másikat!"
        return key
    def SelectRounds(self):
        correct=False
        msg=""
        while correct != True:
            sc =System()
            del sc
            if msg!= "":
                print(msg)
            try:
                size=int(input("Hány körből álljon a játék?"))
            except:
                msg ="Számot kell megadnod!"
            else:
                if size >=1:
                    correct=True
                elif size<1:
                    msg= "Leglább egy kört kell játszanod!"
        return size
    def SelectSize(self):
        correct=False
        msg=""
        while correct != True:
            sc =System()
            del sc
            if msg!= "":
                print(msg)
            try:
                size=int(input("Add meg a pálya nagyságát !"))
            except:
                msg ="Számot kell megadnod!"
            else:
                if size >=2 and size <= 20:
                    correct=True
                elif size<2:
                    msg= "Nagyobb szám kell ennél!"
                else:
                    msg="Kissebb szám kell ennél!"
        return size
    def Statement(self,r,p1,p2,player1,player2):
        sc =System()
        del sc
        print("A játék állás:")
        print()
        print("{}:\t {}".format(player1,p1))
        print()
        print("{}:\t {}".format(player2,p2))
        print("Eddigi körök száma: {}".format(r))
        input("A tovább lépéshez nyomj entert!")
    def Result(self,p1,p2,player1,player2):
        sc =System()
        del sc
        print("A játék eredménye:")
        print()
        if p1 == p2:
            msg ="Döntetlen"
        elif p1 >p2:
            msg="A gyöztes:\t {}".format(player1)
        else:
            msg="A gyöztes:\t {}".format(player2)
        print(msg)
        print()
        input("A tovább lépéshez nyomj entert!")