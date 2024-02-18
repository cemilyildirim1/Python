class benimSinifim:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def kendiFunc(self,sehir):
        self.sehir = sehir
        print("Merhaba benim adım  " + self.name + " yaşadığım yer " +  self.sehir )

    def __str__(self):
        return f"{self.name} , {self.age}"



p1 = benimSinifim("cemil",20)
print(p1)

p1.kendiFunc("istanbul")

print(p1.age)
