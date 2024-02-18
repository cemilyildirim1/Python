import numpy as np
from math import log
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# x = [1,2,3,4]
# y = [4,5,6,7]

# z = []

# # for i,j in zip(x, y):
# #     z.append(i+j)

# z = np.add(x,y)

# print(z)


# def benimfunc(x , y):
#     return x + y

# sayi1 = np.frompyfunc(benimfunc , 2 , 1)

# print(sayi1([1,2,3,4],[5,6,7,8]))


# print(type(np.add))
# print(type(np.concatenate))

# if type(np.add) == np.ufunc:
#     print("add metodu ufunc")
# else:
#     print("değildir")


# arr1 = np.array([1,2,3,-4,-5])
# arr2 = np.array([6,7,8,9,0])
# # z = np.subtract(arr1,arr2)
# # z = np.multiply(arr1,arr2)
# # z = np.divide(arr1,arr2)
# # z = np.power(arr1,arr2)
# # z = np.mod(arr1,arr2)
# z = np.remainder(arr1,arr2)
# z = np.absolute(arr1,arr2)

# print(z)


# arr = np.trunc([-2.133,2.55])
# arr = np.fix([-2.133,2.55])

# arr = np.around([3.6666,1])
# arr = np.around([3.4444,1])

# arr = np.floor([-2.333,2.555])
# arr = np.ceil([-2.1111,2.3333])


# print(arr)

# arr = np.arange(1,10)

# print(np.log2(arr))
# print(np.log10(arr))
# print(np.log(arr))

# benimfunc = np.frompyfunc(log,2,1)

# print(benimfunc(4,2))



# arr1 = np.array([1,2,3])
# arr2 = np.array([1,2,3])

# yeniarr = np.add(arr1,arr2)
# yeniarr = np.sum([arr1,arr2])
# yeniarr = np.sum([arr1,arr2], axis = 1)


# #[1,2,3] = [1, 1+2 , 1+2+3]
# yeniarr = np.cumsum(arr1)



# print(yeniarr)


# arr = [1,2,3,4]
# arr1 = [5,6,7,8]


# print(np.prod([arr,arr1] ))
# print(np.prod([arr,arr1] ,axis=1))

# x = np.cumprod(arr)

# arr = np.array([10,15,25,5])

# x= np.diff(arr)


# print(x)


# num1 = 4 
# num2 = 6 

# arr = np.array([3,6,9])

# # x = np.lcm(num1,num2)       # en küçük ortak kat sayı
# x = np.lcm.reduce(arr)        

# num1 = 6
# num2 = 9
# arr = np.array([20,8,32,36,16])
# x = np.gcd(num1,num2)          # en büyük ortak bölen
# x = np.gcd.reduce(arr)

# arr = np.array([20,8,32,36,16])

# x = np.sin(np.pi/2)
# x = np.sin(arr)


# print(x)
# arr = np.array([20,8,32,36,16])
# # x = np.rad2deg(arr)
# # x = np.deg2rad(arr)

# # x = np.arcsin(arr)

# # taban = 3
# # prep = 4
# # x = np.hypot(taban,prep)


# arr = np.array([1,2,3,4,5,6,6,7,7,7,1,8])
# arr1 = np.array([1,2,3,4,4,5])
# arr2 = np.array([4,4,5,6,7,8])


# x = np.unique(arr)
# x = np.union1d(arr1,arr2)
# x = np.intersect1d(arr1,arr2,assume_unique=True)
# x = np.intersect1d(arr1,arr2,assume_unique=False)
# x = np.intersect1d(arr1,arr2)  # varsayılan flase

# x = np.setdiff1d(arr1,arr2)
# # x = np.setdiff1d(arr2,arr1)
# x = np.setxor1d(arr1,arr2)

# print(x)


# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])
# arr = np.concatenate((arr1,arr2))
# arr = np.hstack([arr1,arr2])

# arr1 = np.array([[1,2,3],[6,7,8]])
# arr2 = np.array([[4,5,6],[9,10,11]])
# arr = np.concatenate((arr1,arr2),axis=1)

# arr = np.array(np.arange(1,9))
# arr1 = np.array([[1,2,3],[6,7,8]])


# # newarr = np.array_split(arr,3)
# newarr = np.array_split(arr1,3,axis=1)
# newarr = np.hsplit(arr1,3)


# print(newarr)
# # print(newarr[0:2])


# arr = np.array([1,2,3,4,5,4,4,6,7,8])
# arr1 = np.array([1,2,3])

# # x = np.where(arr ==4)
# x = np.where(arr%2 == 0)
# y = np.searchsorted(arr,3)
# z = np.searchsorted(arr , 7 , side="left")
# z1 = np.searchsorted(arr1 , 3 , side="right")

# print(z1)

# arr = np.array([2,1,7,8,2,1,2])

# x = np.sort(arr)



# x = [True,False,True,False]

# arr = np.array([8,2,7,4])

# newarr = []

# for i in arr:
#     if i %2== 0:
#         newarr.append(True)
#     else:
#         newarr.append(False)

# x = arr[newarr]        
# arr = np.array([8,2,7,4])

# x = arr %2 == 0
# # x = arr > 4
# y = arr[x]

# print(x)  
# print(y)


# x = random.rand(20)
# x= random.rand(2,3)
# x = random.randint(100)
# x = random.randint(100,size=(3,3))
# y = random.randint(10)

# print(y)
# x = random.choice(y)

# print(x)


# x = random.choice([3,5,7,9],p=[0.1,0.3, 0.6, 0.0],size=(100))

# y = random.choice([3,5,7,9],p=[0.1,0.3, 0.6, 0.0],size=(3,5))

# arr = np.array([1,2,3,4,5])

# # random.shuffle(arr)

# print(arr)
# print(random.permutation(arr))

sns.distplot([0,1,2,3,4,5])

plt.show()
