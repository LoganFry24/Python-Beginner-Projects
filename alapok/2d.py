# sima könyvtár
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
#könyvtár (nested dictonary)
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily) #komplett asszocíativ
print(myfamily["child1"]["name"])
tomb={
    0: {
        "nev": "Jani",
        "kor": 22
    },
    1: {
        "nev": "Dani",
        "kor": 32,
    }
}
print(tomb[1]["nev"])
tomb[2]={}
tomb[2]["nev"] ="Pisti"
#tomb[2]["kor"]=34
print(tomb)
a=2
b="haha"
print("valami {0}".format(a))