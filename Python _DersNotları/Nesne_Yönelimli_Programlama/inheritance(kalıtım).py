class Okul:
    def ders(self):
        print("ders çalıştım")
    def spor(self):
        print("spor yaptım")

class ogrenci(Okul):

    def isim(self):
        print("ben kayak ve kitap okumayı severim.")

ogrenci1 = ogrenci()

ogrenci1.spor()
ogrenci1.ders()
ogrenci1.isim()