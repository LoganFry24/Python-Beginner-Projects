#this is the weakest bot
import random
class Easy:
    def __init__(self,size,lepesek):
        self.size=size
        self.lepesek=lepesek
    def Step(self):
        msg=""
        correct=False
        while correct==False:
            lepes=random.randint(1, self.size**2)
            volt= False
            for x in self.lepesek:
                if x == lepes:
                    volt = True
            if volt == False:
                self.lepesek.append(lepes)
                correct=True
        return msg