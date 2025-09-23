import numpy as np 

arr = np.array([1,2,1,2,4,6,3,2,6,8,9])
print(arr.max()) # Maximum element
print(arr.min()) # Minimum element
print(arr.sum()) # Sum of all elements
print(arr.mean()) # Mean of all elements 
print(np.unique(arr, return_index=True)) # Unique elements 
print(np.unique(arr, return_counts=True)) # Unique elements and their counts

a_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [1, 2, 3, 4]])
print(np.unique(a_2d, axis=0)) # Unique elements in 2D array

narr = np.array([[1,2],
                 [3,4],
                 [5,6]])
print(narr[0,1]) # Accessing element at 0th row and 1st column
print(narr[1:3]) # Slicing rows from index 1 to 2
print(narr[1:2, 0]) # Slicing 1st row and 0th column 