x = lambda a : a+1

print(x(1))


y = lambda a , b : a * b

print(y(4,5))


def function1(x):
    return lambda a ,b: a * b + x

y = function1(4)
print(y(1,2))