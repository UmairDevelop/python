import numpy as np 

ran = np.random.rand(3,3) # 3x3 array of random numbers between 0 and 1
rand = np.random.randn(3,3) # 3x3 array of random numbers from standard normal distribution
randint = np.random.randint(1,10,(3,3))

print(ran)
print(rand)
print(randint)