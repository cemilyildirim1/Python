class Poligon:
    def render(self):
        print("Poligon işleniyor")

class Kare(Poligon):

    def render(self):
        print("Kare işleniyor")

class Yuvarlak(Poligon):
    def render(self):
        print("Yuvarlak işleniyor")


Poligon().render()
Kare().render()
Yuvarlak().render()