import numpy as np

from numpy import random

# d1 = random.randint(100,size = 5)

# print(d1)


# d2 = random.randint(100,size = (3,5))

# print(d2)

# x = random.choice([3,5,7,9],size = (3,5))

# print(x)    

# x = random.normal(loc=5,scale=2,size=3)
# print(x)

arr = np.array([1,2,3,4,5])

print(arr)

random.shuffle(arr)
print(arr)
print(random.permutation(arr))
