import numpy as np

# arr = np.array([1,2,3,])

# print(arr)
# print(type(arr))
# print(np.__version__)

# arr = np.array(23)
# arr = np.array([1,2,3,4,5])
# arr = np.array([[1,2,3,4,5],[12,23,34,14,52]])
# arr = np.array([[[1,2,3,4,5],[12,23,34,14,52]] , [[1,2,3,4,5],[12,23,34,14,52]]])

# print(arr.ndim)

# arr = np.array([12222,2,3,4,5])
# arr = np.array([[1,2,3,4,5],[12,23,34,14,52]])
# arr = np.array([[[1,2,3,4,5],[12,23,34,14,52]] , [[1,2,3,4,5],[12,23,34,14,52]]])

# print(arr[0,1,-5])

# arr = np.array([12222,2,3,4,5,23])
# arr = np.array([[1,2,3,4,5],[12,23,34,14,52]])
# print(arr[1,2:5:2])
# print(arr[1:6:2])


# arr = np.array([12222,2,3,4,5,23],dtype="S")
# arr = np.array([12222,2,3,4,5,23])

# newarr = arr.astype(bool)

# print(newarr)
# print(newarr.dtype)


# arr = np.array([12222,2,3,4,5,23])

# x = arr.copy()
# arr[0] = 42

# print(arr)
# print(x)
# print(x.base)

# x = arr.view()
# arr[0] = 42

# print(arr)
# print(x)
# print(x.base)


# arr = np.array([[12222,2,3,4,5,23],[1,2,3,4,5,6]])
# newarr = arr.reshape(3,4)
# x = newarr.reshape(-1)
# print(x)
# print(newarr.base)


arr = np.array([[12222,2,3,4,5,23],[1,2,3,4,5,6]])

for x in arr:
    for y in x:
        print(y)

for x in np.nditer(arr):
    print(x)