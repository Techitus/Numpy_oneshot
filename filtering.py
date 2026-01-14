import numpy as np

ages = np.array([[21,17,45,67,23],
                 [34,56,15,99,17]])
'''
teenagers = ages[ages < 18]
adults = ages[(ages >= 18) & (ages < 65)]
evens = ages[ages % 2 == 0]
odds = ages[ages % 2 != 0]
print(teenagers) #[17 15 17]
print(adults) #[21 45 23 34 56]
'''

#Where functions (keeps original array)
adults = np.where(ages >= 18, ages, 0)
print(adults) #[[21  0 45 67 23] [34 56  0 99  0]]
