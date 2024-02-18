

kilo = float(input("Kilo gir :"))
boy = float(input("Boy gir :"))

if type(boy) == int :
    boy = float(boy / 100)

if type(boy) == float :
    pass

index = kilo / (boy**2)
print(index)
if(index < 18.50):
    print("Zayıf")
    alınacakIndex = 18.50 - index
    alınacakKilo = alınacakIndex * (boy**2)
    print("Alınması gereken kilo :  ",alınacakKilo)
elif(index >= 18.50 and index <= 24.99 ):
    print("Sağlıklı kilo")
elif(index >= 25 and index <= 29.99):
    verilecekIndex = index - 24.99
    verilecekKilo = verilecekIndex * (boy ** 2)
    print("Aşırı kilo")
    print("Verilmesi gereken kilo :  ", verilecekKilo)
elif(index >= 30):
    verilecekIndex = index - 24.99
    verilecekKilo = verilecekIndex * (boy ** 2)
    print("Obez  ")
    print("Verilmesi gereken kilo :  ", verilecekKilo)



