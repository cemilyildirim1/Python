import json
import numpy as np
import matplotlib.pyplot as plt
dosya1 = open("idx1.json","r",encoding="utf-8")
dosya2 = open("idx5.json","r",encoding="utf-8")
dosya_ayar = open("ayar.json","r",encoding="utf-8")



idx1 = json.load(dosya1)
idx5 = json.load(dosya2)
ayar = json.load(dosya_ayar)

temp = idx1["result"][0]["Temp"]
humidity = idx1["result"][0]["Humidity"]
data = idx5["result"][0]["Data"]


#alt sınır üst sınır denetmele  (SICAKLIK)
sıcaklık_alt_sinir = ayar["icsAlt"]
sıcaklık_ust_sinir = ayar["icsUst"]

height = [temp, humidity, data]
bars = ('TEMP', 'HUMİDİTY', 'DATA')
x_pos = np.arange(len(bars))



plt.bar(x_pos,temp)
plt.xticks(x_pos,bars)
plt.show()
if(temp <= sıcaklık_alt_sinir):
    print("Sıcaklık sınırın altında.")
elif(temp >= sıcaklık_ust_sinir):
    print("Sıcaklık sınırın üstünde.")
else:
    print("Sıcaklık değerler arasındadır.")


#alt sınır üst sınır denetmele  (NEM)
    
nem_alt_sinir = ayar["icnAlt"]
nem_ust_sinir = ayar["icnUst"]

if(humidity <= nem_alt_sinir):
    print("Nem sınırın altında.")
elif(humidity >= nem_ust_sinir):
    print("Nem sınırın üstünde.")
else:
    print("Nem değerler arasındadır.")

#alt sınır üst sınır denetmele  (DATA)
    
data_alt_sinir = ayar["co2Alt"]
data_ust_sinir = ayar["co2Ust"]
data_sayi = data[:2]

if(int(data_sayi) <= data_alt_sinir):
    print("Data sınırın altında.")
elif(int(data_sayi)  >= data_ust_sinir):
    print("Data sınırın üstünde.")
else:
    print("Data değerler arasındadır.")



 





# # Create dataset
# height = [3, 12, 5, 18, 45]
# bars = ('A', 'B', 'C', 'D', 'E')
# x_pos = np.arange(len(bars))
 
# # Create bars
# plt.bar(x_pos, height)
 
# # Create names on the x-axis
# plt.xticks(x_pos, bars)
 
# # Show graphic
# plt.show()