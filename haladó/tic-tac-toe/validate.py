#check the correction of the input
from system import System
class Validate:
    def __init__(self,msg):
        self.var=""
        self.msg=msg
    def check(self):
        msg=""
        correct =False
        while correct!=True:
            sc=System()
            del sc
            #validate the difficulty level input
            if self.msg=="Kérem a nehézségi szint számát!":
                print("Választható nehézségi szintek:")
                print("Könnyű: 1")
                print("Normál: 2")
                print("Nehéz: 3")
                print(msg)
                msg=""
                try:
                    self.var=int(input(self.msg))
                except:
                    msg="Egészszámot kell megadnod nehézségi szintnek!"
                else:
                    if  int(self.var)>0 and int(self.var)<4:
                        correct=True
                        return self.var
                    elif int(self.var)>3 or int(self.var)<1:
                        msg="Ilyen számú nehézségi szint nem létezik. Kérlek adj meg egy létezőt!"
            else: #case of string input (names)
                if msg!= "":
                    print(msg)
                self.var=input(self.msg)
                if len(self.var) >0 and self.var[0]!=' ' and self.var[0]!='\t' and self.var != "Computer":
                    correct=True
                    return self.var
                elif self.var == "Computer":
                    msg = "Ez az AI neve. Te nem használhatód ezt!"
                else:
                    msg = "Muszály megadnod egy nevet!"