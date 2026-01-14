import numpy as np

#scalar arithematic
'''
arr =np.array([1,2,3])

print(arr + 2)  #add 2 to each element
print(arr - 1)  #subtract 1 from each element
print(arr * 3)  #multiply each element by 3
print(arr / 2)  #divide each element by 2
print(arr ** 2) #square each element

print(np.sqrt(arr)) #square root of each element
print(np.floor(arr)) #floor value of each element
'''
#Exercise
'''
radii =np.array([1,2,3])
area = np.pi * radii ** 2
print(area)
'''

#Element wise arithematic
'''
array1= np.array([1,2,3])
array2 = np.array([4,5,6])
print(array1 + array2) #[5 7 9]
'''

#comparision operators
scores = np.array([91,55,100,73,82,64])
print(scores == 100) #[False False  True False False False]
print(scores  > 60) #[ True False  True  True  True  True]
