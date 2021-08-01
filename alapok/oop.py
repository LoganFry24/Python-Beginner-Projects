#Írjunk egy olyan osztályt, amely számolja, hogy hányszor példányosítottuk.
class Program():
    def __init__(self,i):
        self.i=i
    def Count(self):
        return self.i+1
i=0
p1=Program(i)
i=p1.Count()
p2=Program(i)
i=p2.Count()
p3=Program(i)
print(p3.Count())