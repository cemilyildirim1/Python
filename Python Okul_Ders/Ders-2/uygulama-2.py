from random import randint


kolon = int(input("kaç kolon oluşturmak istiyorsunuz"))
liste_buyuk = []
liste = []


for i in range(kolon):
    for x in range(6):
        rastgeleSayi = randint(1,90)
        liste.append(rastgeleSayi)

    liste_buyuk.append(liste)
    



print(liste_buyuk)



