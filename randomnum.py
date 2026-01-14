import numpy as np
'''
#rng = np.random.default_rng()
rng = np.random.default_rng(seed = 0) #seed le everytime same random number generate grxa seed ko value j vyeni frk prdaina

print(rng.integers(1,7)) #second number is exclusive
#OR
print(rng.integers(low=1,high=101,size=3)) #[68 35 55]
print(rng.integers(low=1,high=101,size=(3,2))) #[[18 23] [13 47] [21 32]]


print(np.random.uniform()) #o and 1 ko bich ko random value
print(np.random.uniform(low=-2,high=1))
'''
#suffle
'''
array = np.array([1,2,3,4,5])
rng = np.random.default_rng()
rng.shuffle(array)
print(array) #randomly suffle eg [4 1 3 2 5]
'''
#choice
rng = np.random.default_rng()
fruits = np.array(['Apple','Banana','Orange','Pineapple'])
fruit = rng.choice(fruits ,size=3)
print(fruit) #randomly choose


