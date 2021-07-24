#check the status of the game
from levelgenerator import Levelgen
l=Levelgen(20)
level=l.Generate()
for x in level:
    print(x)
i=0
while i!=len(level):
    x=0
    while x!=len(level[i]):
        """
        if level[i][x]=='1' and level[i][x+1]=='0' and level[i][x+2]=='0': #1.modszer
            print("{}{}{}".format(level[i][x],level[i][x+1],level[i][x+2]))
        """
        if x<len(level[i])-2: #2.modszer
            sor = "{}{}{}".format(level[i][x],level[i][x+1],level[i][x+2])
            if sor == "400":
                print("megvan")
                print(sor)
                level[i][x]=' '
                level[i][x+1]='X'
                level[i][x+2]=' '
        x+=1
    i+=1
for x in level:
    print(x)