#check the status of the game
from levelgenerator import Levelgen
l=Levelgen(20)
level=l.Generate()
width=len(level[0])
track= [[0 for x in range(width)]for y in range(len(level))]
i=0
while i!=len(level):
    x=0
    while x!= len(level[i]):
        track[i][x]=level[i][x]
        x+=1
    i+=1

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
                track[i][x]=' '
                track[i][x+1]='X'
                track[i][x+2]=' '
        x+=1
    i+=1
i=0
while i!=len(level):
    x=0
    sor=""
    while x!=len(track[i]):
        sor="{}{}".format(sor,track[i][x])
        x+=1
    level[i]=sor
    i+=1
for x in level:
    print(x)