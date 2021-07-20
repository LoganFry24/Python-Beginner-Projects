db=len(open("ub2017egyeni.txt").readlines())
db-=1
file= open("ub2017egyeni.txt","rt")
adat=[[0 for x in range(5)] for y in range(db)]
i=0
file.readline()
a=0
b=0
c=0
d=[]
e=[]
def IdőÓrában(ido):
    h=int(ido.split(":")[0])
    m=int(ido.split(":")[1])
    s=int(ido.split(":")[2])
    h= h+m/60+s/3600
    return h
while i!= db:
    sor=file.readline()
    adat[i][0]= sor.split(";")[0]
    adat[i][1]= sor.split(";")[1]
    adat[i][2]= sor.split(";")[2]
    adat[i][3]= sor.split(";")[3]
    adat[i][4]= sor.split(";")[4].strip()
    if adat[i][2] == "Noi" and adat[i][4] == '100':
        a+=1
        d.append(i)
    if adat[i][2] == "Ferfi" and adat[i][4] == '100':
        b+=1
        c+=IdőÓrában(adat[i][3])
        e.append(i)
    i+=1
file.close()
print("3.feladat: egyéni indulok száma: {} fő".format(db))
print("4.feladat. Célba érkezett nők száma: {} fő".format(a))
nev =input("Kérem a sportoló nevét:")
i=0
indult = "Nem"
telj= "Nem"
while i!=db:
    if adat[i][0] == nev:
        indult= "Igen"
        if adat[i][4]=='100':
            telj="Igen"
    i+=1
print("\t Indult egyéniben a sportoló?"+indult)
print("\t Teljesítette a teljes távot?"+ telj)
print("7.feladat: Átlagos idő: {} óra".format(c/b))
f=d[0]
for x in d:
    if IdőÓrában(adat[f][3])> IdőÓrában(adat[x][3]):
        f=x
print("Nők: {} ({}.) - {}".format(adat[f][0],adat[f][1],adat[f][3]))
f=e[0]
for x in e:
    if IdőÓrában(adat[f][3])> IdőÓrában(adat[x][3]):
        f=x
print("Férfiak: {} ({}.) - {}".format(adat[f][0],adat[f][1],adat[f][3]))