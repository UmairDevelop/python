import numpy as np

arr = np.array([3,2,32,1,2,4,5])
narr = arr[:-3] # All elements except last 3
print(narr) 

arr1 = np.array([[1,2],
                 [3,4]])
arr2 = np.array([[5,6],
                 [7,8]])
arr3 = np.vstack((arr1, arr2)) # Vertical stacking (along rows)
arr3 = np.hstack((arr1, arr2)) # Horizontal stacking (along columns)
print(arr3)

n = np.arange(1, 25).reshape(2,12) # 2D array of shape (2,12)
n = np.hsplit(n, 4) # Split into 4 arrays horizontally
print(n) 