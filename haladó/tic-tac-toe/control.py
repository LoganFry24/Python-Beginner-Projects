#game controls
class Controls:
    def __init__(self,mode):
        self.mode=mode
    def Input(self,turn,size,lepesek):
        if self.mode =="S" and turn=="computer":
            msg=self.Bot(size)
            return msg
        else:
            msg=self.Human(size,lepesek)
            print(msg)
            return msg
    def Human(self,size,lepesek):
        correct=False
        msg=""
        while correct != True:
            try:
                lepes=int(input())
            except:
                print("Egészszámot kell megadnod!")
            else:
                volt=False
                for x in lepesek:
                    if x==lepes:
                        volt=True
                if lepes <= size**2 and lepes >=1 and volt==False:
                    lepesek.append(lepes)
                    correct=True
                    return msg
                elif volt==True:
                    msg="Ez a hely már foglalt! Adj meg egy másikat"
                    return msg
                else:
                    msg="Ilyen hely nincs! Adj meg egy létezőt!"
                    return msg
        
    def Bot(self,size):
        pass