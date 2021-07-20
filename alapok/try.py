import random 
error = random.randint(0,5) # hiba kód generálás
msg="Hiba kód 6"
memmory=False
network=False
connection=False
outrange=False
def elso():
    print("szia")
#hiba generálása hiba kód alapján
if error!=1: # ha nincs deklarálási probléma probléma
    x="Hello világ!"
if error==1: # deklarálási probléma
    msg="Hiba kód 1"
if error==2: #fatal error hiba
    memmory=True
    msg="Hiba kód 2"
if error==3: #hálózati hiba
    network=True
    msg="Hiba kód 3"
if error==4: #csatlakozási hiba
    connection=True
    msg="Hiba kód 4"
if error==5:
    outrange=True
    msg="Hiba kód 5"
print("A teszt generált hiba kódja {}".format(error))
try:
    print(x)
    if memmory==True or outrange == True or network==True or connection==True:
        raise Exception("error")
except NameError:
    print(msg)
    print("Az üzenet változó nincs deklarálva")
except:
    print(msg)
    if memmory == True:
        print("Fatal Error")
    elif network==True:
        print("Hálózati hiba")
    elif connection==True:
        print("Nem sikerült csatlakozni")
    elif outrange==True:
        print("Intervallumon kivüli értéket vett fel a program!")
    else:
        print("Egyéb hiba lépet fel!")
else:
    print("Nincs probléma")
finally:
  print("Az ellenőrzés kész")
