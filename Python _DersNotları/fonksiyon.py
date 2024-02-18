# *x = args  ,  **x = kwargs
"""def fonksiyonum(*x):
    print(" fonksiyon " + x[2] + " çalıştı ")

fonksiyonum("kötü","iyi","çok iyi")

def fonksiyonum2(**x):
    print( x["rz"] + " fonksiyon")

fonksiyonum2( rz = " Rize")


def func(x):
    for sayi in x :
        print(sayi)

Sayilar = [1,2,3,4,5]

func(Sayilar)"""


def function3(x):
    sayi = x + 2
    print(sayi)
    return sayi
    function3(sayi)

function3(1)

function3(1)