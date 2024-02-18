iller =[("Tekirdağ",120),("Ankara",664),("Çanakkale",233),("Bursa",436),("Mersin",1143)]

uzaklik = input("Uzaklığı giriniz : ")
uzaklik= float(uzaklik) * 1.6

uzaklik_mil = filter((map(lambda x  : x[1] > uzaklik ,iller)))




print(uzaklik_mil)