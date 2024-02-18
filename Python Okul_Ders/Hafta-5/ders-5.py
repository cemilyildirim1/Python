#list comprehension

# liste1 = [sayi for sayi in range(101)]
# print(liste1)

# name = "Cemil"
# sonuc =[eleman for eleman in name]
# print(sonuc)

# liste2 = [sayi*2 for sayi in liste1]
# print(liste2)

# liste1 = [0,1,2,3,4,5,6]
# liste2 = [sayi**2 for sayi in liste1 if sayi%2==0 ] 
# print(liste1,liste2)

# obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
# print(obj)


# matrix = []

# for sayi in range(5):
#     matrix.append([])
#     for sayi2 in range(5):
#         matrix[sayi].append(sayi2)
# print(matrix)

# matrix = [[sayi1 for sayi1 in range(5)]  for i in range(5)]
# print(matrix)


# Generators
# def func():
#     yield 1
#     yield 2
#     yield 3

# a = {sayi for sayi in func()}
# print(a)

# def yuzler():
#     num = 100
#     while(num < 1000):
#         yield num
#         num+=100

# sonuc = [sayi for sayi in yuzler()]
# print(sonuc)


# def generator():
#     yield 1
#     yield 2
#     yield 3
# a = generator()
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())

# def yuzler():
#     num =100
#     while(num < 1000):
#         yield num
#         num +=100
# a = yuzler()
# for sayi in a :
#     print(sayi)
# print(next(a)) # hata

# gen = [i**2 for i in range(100)]
# print(sum(gen))
# print(sum(gen))

# gen = (i**2 for i in range(100))
# print(sum(gen))
# print(sum(gen))

# def infinite_sequance():
#     num = 0
#     while True:
#         yield num
#         num +=1
# a = infinite_sequance()
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

#Generator Expressions

import sys
nums_squared_lc = [i*2 for i in range(10000)]
print(sys.getsizeof(nums_squared_lc))

nums_squared_gc = (i*2 for i in range(10000))
print(sys.getsizeof(nums_squared_gc))


