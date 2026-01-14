import numpy as np 

#lists
'''
my_list = [1,2,3,4]
print(my_list)
'''
#array
'''
my_array = np.array([1,2,3,4,5])
dounble_my_array = my_array * 2
print(dounble_my_array)
print(my_array)
'''
#Multidimensional Array
'''
my_3d_array = np.array([[[1, 2, 3], [4, 5, 6]],[[7, 8, 9], [10, 11, 12]]])
print(my_3d_array)
print(my_3d_array.ndim) #dimension is 3
print(my_3d_array.shape) #shape is (2, 2, 3) that means 2 blocks, 2 rows, and 3 columns
print(my_3d_array[0,0,1]) #2
number = my_3d_array[1,1,2] + my_3d_array[0,1,2]
print(number) #12 + 6 = 18
'''

#slicing
array = np.array([[1,2,3,4],[5,6,'A','B'],["C","D","E","F"]])
#slicing = array[start:end:step]
#print(array[::-1]) #reverse the array
#first index is for rows and second index is for columns
print(array[:,:2])
