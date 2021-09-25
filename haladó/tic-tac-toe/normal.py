#this is a regular bot
import math
import random
class Normal:
    def __init__(self,size,lepesek):
        self.size=size
        self.lepesek=lepesek
    def Step(self):
        correct=False
        mid =True
        while correct == False:
            #first step
            if len(self.lepesek)==1 and mid == True: # try to get the middle point
                lepes = self.GetMid()
                correct= self.Check(lepes)
                mid = False
            elif len(self.lepesek)==1: # find another starting point
                lepes= self.First()
                correct= self.Check(lepes)
            else: #after the first turn
                lepes= self.First()
                correct= self.Check(lepes)
        self.lepesek.append(lepes)
    def GetMid(self):
        # the size is a even number
        if (self.size**2) % 2 ==0:
            self.side=random.randint(1,4)
            #left side
            if self.side ==1:
                lepes = 1
                if self.Check(lepes)==False:
                    self.side =2
            if self.side == 2:
                lepes = self.size
                if self.Check(lepes)==False:
                    self.side =3
            if self.side == 3:
                lepes = self.size
                if self.Check(lepes)==False:
                    self.side =4
        else: # the size is a odd number
            return math.ceil(self.size**2/2)
    def First(self):
        lepes=random.randint(1, self.size**2)
        return lepes
    def Check(self,lepes):
        volt= False
        for x in self.lepesek:
            if x == lepes:
                volt = True
        if volt == False:
            return True
        else:
            return False
"""          
size=5
lepesek=[13]
con = Normal(size,lepesek)
con.Step()
print(lepesek)
"""