import numpy as np

#Broadcasting allows numpy to perform operation on arrays

array1 = np.array([[1,2,3,4,5]])
array2 = np.array([[1],[2],[3],[4]])
print(array1.shape) #(1,5) #first is row second is column
print(array2.shape) #(4,1)

print(array1 * array2)
#for dimension shape  should same, OR One of them is 1