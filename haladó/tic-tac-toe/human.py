class Human:
    def __init__(self,size,lepesek):
        self.size=size
        self.lepesek=lepesek
    def GetInput(self,size,lepesek):
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