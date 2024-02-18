# a = lambda a,b : a**b

# print(a(2,3))

# def func(n):
#     return lambda a : a**n

# sonuc = func(4)

# print(sonuc(2))

dizi1 = [1,2,3,4]
dizi2 = [11,12,13,14]

a = list(map(lambda x : x**2 ,dizi1))
a = list(map(lambda x,y : x+y ,dizi1 ,dizi2 ))
a = list(filter(lambda x : x % 2 ==0 ,dizi2))


print(a)

