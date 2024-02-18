class Bilgisayar:

    def __init__(self):
        self.__maxfiyat = 10000     # "__" ifedesi özel olduğu anamına geliyor.Direkt nesene dışarıdan değiştirilemez.Fonksiyon ile değiştirilebilir.#

    def satis(self):
        print("bilgisayar şu fiyata satılıyor" , self.__maxfiyat)

    def fiyatDegistir(self,ucret):
        self.__maxfiyat = ucret


x = Bilgisayar()
x.satis()

x.maxfiyat = 15000
x.satis()

x.fiyatDegistir(15000)
x.satis()
