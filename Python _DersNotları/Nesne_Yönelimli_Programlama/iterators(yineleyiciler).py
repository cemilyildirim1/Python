"""benimtuple = (1,2,3)

x = iter(benimtuple)

print(next(x))
print(next(x))
print(next(x))"""

class BenimSayim:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

benimSinifim = BenimSayim()
z = iter(benimSinifim)

print(next(z))
print(next(z))
print(next(z))
print(next(z))
print(next(z))
