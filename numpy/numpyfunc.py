import numpy as np 

zero = np.zeros((3,3)) # 3x3 array of all zeros
ones = np.ones((2,2), dtype=np.int32) # 2x2 array of all ones
cus = np.full((2,2), 8) # 2x2 array of all 8s
eye = np.eye(3) # 3x3 Identity matrix   
arrange = np.arange(1,15,2) # 1 to 15 with step of 2
linspace = np.linspace(1,10,5) # Evenly spaced 5 numbers from 1 to 10
empty = np.empty((2,2)) # 2x2 array with random values (uninitialized values)

print(zero)
print(ones)
print(cus)
print(eye)
print(arrange)
print(linspace)
print(empty)