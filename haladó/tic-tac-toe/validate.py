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
            if self.msg=="Kérem a nehézségi szint számát!":
                print("Választható nehézségi szintek:")
                print("Könnyű: 1")
                print("Normál: 2")
                print("Nehéz: 3")
                print(msg)
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
            else: #case of string input
                self.var=input(self.msg)
                if len(self.var) >0 and self.var[0]!=' ' and self.var[0]!='\t':
                    correct=True
                    return self.var  