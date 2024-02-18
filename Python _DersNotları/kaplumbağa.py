import turtle
import random


#harita çizimi
t = turtle.Turtle()
t.up()
t.goto(-100,100)
t.down()
t.speed(0)


for i in range(15):
    t.write(i)
    t.right(90)
    t.forward(200)
    t.left(180)
    t.forward(200)
    t.right(90)
    t.forward(20)
    
#ilk yarışmacıyı oluşturma

ilk = turtle.Turtle()
ilk.shape("turtle") 
ilk.color("red")
ilk.up()
ilk.goto(-120 , 70)
ilk.down()
    
#ikinci yarışmacıyı oluşturma

ikinci = turtle.Turtle()
ikinci.shape("turtle")
ikinci.color("blue")
ikinci.up()
ikinci.goto(-120 , 40)
ikinci.down()

#üçüncü yarışmacıyı oluşturma

ucuncu = turtle.Turtle()
ucuncu.shape("turtle")
ucuncu.color("yellow")
ucuncu.up()
ucuncu.goto(-120 , 10)
ucuncu.down()

x = random.randint(1 , 10)

for i in range(x):
    fan = turtle.Turtle()
    fan.shape("turtle")

    # r = random.randint(0 , 255)
    # g = random.randint(0 , 255)
    # b = random.randint(0 , 255)
    # fan.color(r,g,b)


    fan.up()
    fan.goto(-90+25*i,-120)
    fan.down()
    fan.left(90)

x_ilk    = 0
x_ikinci = 0
x_ucuncu = 0

tahmin = input("Hangi kaplumbağa kazanacak ? ")

yazi = turtle.Turtle()
yazi.up()
yazi.goto(-120 , 120)
yazi.down()
yazi.write("Kazanmasını istediğin oyuncu : "+ tahmin)

kazanan = turtle.Turtle()




while(True):
    if (x_ilk > 305):
        kazanan.up()
        kazanan.goto(-120 , 150)
        kazanan.down()
        kazanan.write("YARIŞI İLK KAPLUMBAĞA KAZANDI")
        break
    if (x_ikinci > 305 ):
        kazanan.up()
        kazanan.goto(-120 , 150)
        kazanan.down()
        kazanan.write("YARIŞI İKİNCİ KAPLUMBAĞA KAZANDI")
        break
    if (x_ucuncu > 305):
        kazanan.up()
        kazanan.goto(-120 , 150)
        kazanan.down()
        kazanan.write("YARIŞI ÜÇÜNCÜ KAPLUMBAĞA KAZANDI")
        break
    sayi1 = random.randint(1,5)
    x_ilk += sayi1
    ilk.forward(sayi1)

    sayi2 = random.randint(1,5)
    x_ikinci += sayi2
    ikinci.forward(sayi2)

    sayi3 = random.randint(1,5)
    x_ucuncu += sayi3
    ucuncu.forward(sayi3)



turtle.done()