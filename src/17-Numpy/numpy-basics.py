import numpy as np

#numpy normal klasik dizilerden daha kolay kullanıslı sistemler icin kllnlr

# python list
py_list = [1,2,3,4,5,6,7,8,9]

# numpy array
np_array = np.array([1,2,3,4,5,6,7,8,9])

print(type(py_list))
print(type(np_array))

py_multi = [[1,2,3],[4,5,6],[7,8,9]]
np_multi = np_array.reshape(3,3)  #matrix

print(py_multi)
print(np_multi)

#boyutlara bakmak : ilki tek boyut digeri 2 boyutlu yani matrix
print(np_array.ndim)
print(np_multi.ndim)

#sekilleri : ilki 9 doner ikincisi 3,3 doner
print(np_array.shape)
print(np_multi.shape)





