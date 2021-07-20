import os
class Levelgen:
    def __init__(self,size):
        self.size=size
        if self.size <2:
            raise Exception("Hiba! A pálya mérete túl kicsi!")
        elif self.size > 20:
            raise Exception("Hiba! A pálya mérete túl nagy!")
        else:
            pass
    