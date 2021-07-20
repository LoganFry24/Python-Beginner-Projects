def Harom():
    a=int(input("Kérek egy számot!"))
    if a % 3 ==0:
        print("A megadott szám osztható 3-mal.")
    else:
        print("A megadott szám nem oszható 3-mal.")
def Hatvany():
    a=int(input("Kérek egy hatvány alapot!"))
    b=int(input("Kérek egy hatvány kitevőt!"))
    print("a hatvány: {}".format(a**b))
import random
t=[]
i=0
while i!=10:
    t.append(random.randint(1, 100))
    i+=1
def Min():
    print("a tömb elemei:")
    print(t)
    i=1
    m=t[0]
    while i!=10:
        if t[i]< m:
            m=t[i]
        i+=1
    print("A legkissebb elem a tömben: {}".format(m))
def Max():
    print("a tömb elemei:")
    print(t)
    i=1
    m=t[0]
    while i!=10:
        if t[i]> m:
            m=t[i]
        i+=1
    print("A legnagyobb elem a tömben: {}".format(m))
def Szoveg():
    a=input("Kérek egy szöveget!") [::-1]
    print(a)
    print(len(a))
def Datum():
    a=input("Kérek dátumot yyyy-mm-dd formában!")
    y, m ,d =map(int, a.split("-"))
    import datetime
    a=datetime.date(y, m,d) 
    ma=datetime.date.today()
    print(ma, a)
    if ma> a:
        a=ma-a
        print("A megadott dátum {} napja volt".format(a.days))
    elif ma==a:
        print("A megadott dátum a mai dátum.")
    else:
        a=a-ma
        print("A megadott dátum {} nap múlva lesz.".format(a.days))
def kek():
    a=input("Kérem a függvény számát!")
    if a== '1':
        Harom()
        kek()
    elif a== '2':
        Hatvany()
        kek()
    elif a== '3':
        Min()
        kek()
    elif a== '4':
        Max()
        kek()
    elif a== '5':
        Szoveg()
        kek()
    elif a== '6':
        Datum()
        kek()
    else:
        print("Helytelen függvény szám!")
        kek()
kek()
