#declare the arrays for testing
arrayk = [111,121,44,33,21,18,374,571,681,"WEW"] #wrong array
arrayn=[111,121,44,33,21,18,374,571,681.1]
arrayc=["hgurh","k","a","fa","ff","A"]
# the sorting function
def sort(array,t):
    db=len(array)
    # define the abc with upper and lowercases
    import string
    s=list(string.ascii_lowercase)
    b=list(string.ascii_uppercase)
    i=0
    abc=[]
    while i!=len(s):
        abc.append(s[i])
        abc.append(b[i])
        i+=1
    # it's a full handmade indexof function to get the letter's position from the abc 
    def index(temp):
        k=0
        while k!=len(abc):
            if abc[k]==temp:
                index=k
            k+=1
        return index
    #this is the ascending sorting function
    def asc(t1):
        i=0
        while i!=db:
            e=i+1
            while e!=db:
                # if the array type is integer or float (numerical)
                if t1==int:
                    if array[i]>array[e]:
                        temp=array[i]
                        array[i]=array[e]
                        array[e]=temp
                # if the array type is string or char
                else:
                    x=0
                    #we have to know which word is the larger or we will got a index is out of range error message
                    if len(array[i]) < len(array[e]):
                        hosz=len(array[i])
                    else:
                        hosz=len(array[e])
                    while x!=hosz:
                        if index(array[i][x]) > index(array[e][x]):
                            temp=array[i]
                            array[i]=array[e]
                            array[e]=temp
                        x+=1
                e+=1              
            i+=1
    #descending sorting method
    def desc(t1):
        i=0
        while i!=db:
            e=i+1
            while e!=db:
                # if the array type is integer or float (numerical)
                if t1==int:
                    if array[i]<array[e]:
                        temp=array[i]
                        array[i]=array[e]
                        array[e]=temp
                 # if the array type is string or char
                else:
                    x=0
                    #we have to know which word is the larger or we will got a index is out of range error message
                    if len(array[i]) < len(array[e]):
                        hosz=len(array[i])
                    else:
                        hosz=len(array[e])
                    while x!=hosz:
                        if index(array[i][x]) < index(array[e][x]):
                            temp=array[i]
                            array[i]=array[e]
                            array[e]=temp
                        x+=1
                e+=1              
            i+=1
    def check(t1):
        if t=="asc":
            asc(t1)
        elif t=="desc":
            desc(t1)
        else:
            raise Exception("Hibás értékű a második atributum.")
            # you have to choose between ascending and descending there is no other way!!!
    #check the type of array
    def checkarray():
        def ty(t1,t2):
            i=1
            while i!=db: #check
                if type(array[i]) is t1 or type(array[i]) is t2:
                    i+=1 
                    #the type of all element is the same (numerical or text)
                else:
                    raise Exception("Hiba! A tömb csak egy típusból állhat!")
                    # we have found another type so we have to print a error message to the terminal
            check(t1) 
        # if the first element of our array is a string or a char then we want to know that every element of the array are also a string or a char
        if type(array[0]) is str or type(array[0]) is chr:
            ty(str,chr)
        # if the first element of our array is an integer or a float then we want to know that every element of the array are also an integer or a float
        elif type(array[0]) is int or type(array[0]) is float: 
            ty(int,float)
    # that's the starting pont of our function
    checkarray()
    return array
# invite the sorting function
print(sort(arrayn,"desc"))