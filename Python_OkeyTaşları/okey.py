import random as rnd

okey_taslari = [tas_renk+str(sayi) for tas_renk in ("kırmızı-","mavi-","sarı-","turuncu-") for sayi in range(1,14)] * 2


def tas_cek():
    while True:
        rastgele = rnd.randint(0,len(okey_taslari)-1)
        yield okey_taslari[rastgele]
        del okey_taslari[rastgele]

tasim = tas_cek()

print(next(tas_cek()))
try:
    while True :
        print(f'Çekilen {next(tasim)} , kalan tas {len(okey_taslari)}')
except Exception as s:
    print("Üzgünüm , taş bitti.")
    print(s)


