"""def myfunc():
    x = 200
    print(x)
    def myfunc1():
        print(x)

    myfunc1()

myfunc()"""

x = 300

def func():
    global x
    x = 2000
    print(x)

func()
print(x)