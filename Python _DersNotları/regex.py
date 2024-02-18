import re

# x = "Merhaba benim adım Berk"

# y = re.search(r"Berk",x)


# print(y.start())
# print(y.end())

# print(y)

cumle = "Merhaba  19 numaralı sayı  ile 23 numaralı sayıların çarpımı nedir . "

regex = "\d+"                    #cümle içindeki sayıları getirir
regex = "\d"                     #cümle içindeki rakamları getirir


x = re.findall(regex,cumle)      # cumle değişkenin de regex değişkenini arar

# x = re.compile('[e - a]')        # cümle içinde e  ve a değerlerini getirir

# y = x.findall("Merhaba  19 numaralı sayı ile 23 numaralı sayıların çarpımı nedir . ")

x = re.compile("\w")    #cümle içindeki  karakterleri getirir
x = re.compile("\w+")   #cümle içideki kelimeleri getirir
x = re.compile("\W")    #cümle içideki yabancı karakterleri getirir
x = re.compile("r")   #içinde "r" olan kelime kadar eleman dödürür


# print(x.findall("örnek cümle örnekler örn - _ 0 * 9 "))      

# print(re.split("\W","bu * bir * örnek cümledir"))

# print(re.split("örnek","Bu bir örnek cümledir"))

x = "Merhaba python dersine"

y = re.search(r"\bp",x)

print(y.re)
print(y.string)

