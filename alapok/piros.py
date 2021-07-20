tup=("Franklin Goodman","Dwight Hart","Shelia Meyer","Reginald White","Sheldon Jenkins","Francisco Nash","Jan Cross","Jesse Ferguson","Bob Franklin","Miriam Mccarthy")
import random
file=open("file.txt","w")
i=0
while i!=len(tup):
    file.write("{};{};{}\n".format(i+1,tup[i],random.randint(18,70)))
    i+=1
file.close()
adat={}
db=len(open("file.txt").readlines())
file=open("file.txt", "rt")
i=0
a=0
tomb=[]
while i!=db:
    sor=file.readline()
    adat.setdefault(i, {})["id"] =sor.split(";")[0]
    adat.setdefault(i,{})["nev"] =sor.split(";")[1]
    adat.setdefault(i,{})["kor"] = int(sor.split(";")[2])
    a+=adat[i]["kor"]
    tomb.append(adat[i]["kor"])
    i+=1
file.close()
print("Az emberek átlag életkora {:.2f}".format(a/db))
m=min(tomb)
i=0
while i!=db:
    if m==adat[i]["kor"]:
        print("A legfiatalabb ember: {} aki {} éves".format(adat[i]["nev"],m))
        break
    i+=1
m=max(tomb)
i=0
while i!=db:
    if m==adat[i]["kor"]:
        print("A legidősebb ember: {} aki {} éves".format(adat[i]["nev"],m))
        break
    i+=1
nev= input("Kérek egy nevet")
i=0
while i!=db:
    if nev==adat[i]["nev"]:
        print("A sorszáma: {}".format(adat[i]["id"]))
        break
    i+=1