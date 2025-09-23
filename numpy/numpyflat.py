import numpy as np

arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
arr2 = arr.flatten() # Converts 2D array to 1D array
print(arr2) # But the original array remains unchanged

narr = arr.copy() # Creates a copy of the array
narr2 = narr.ravel() # Another way to flatten the array
narr2[0] = 99 
print(narr) # Change to the copy affects the original as well