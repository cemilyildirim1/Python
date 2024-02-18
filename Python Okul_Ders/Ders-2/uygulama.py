print("ALt sınır ve üst sınır limitlerini giriniz")

alt_sınır = int(input("Alt sınırı giriniz : "))
ust_sınır = int(input("Ust sınırı giriniz : "))

list_asal = []


for sayi in range(int(alt_sınır) ,int(ust_sınır)+1):
    if sayi > 1:
        for bolen in range(2,sayi):
            if(sayi % bolen == 0):
                break
            else:
                list_asal.append(sayi)
                break
    else:
        list_asal.append(sayi)
        break

print(list_asal)

         

