import numpy as np 

arr = np.array([3,2,32,1,2,4,5])
# arr = np.sort(arr) # Ascending order
# arr = np.sort(arr)[::-1] # Descending order
# arr = np.argsort(arr) # Gives the indexes that would sort the array

surname = ["ahmad", "raza", "usman"]
firstname = ["umair", "ali", "ayesha"]
age = [19, 27, 20]
arrr = np.lexsort((surname, firstname, age)) # Sort by firstname, then by surname
for i in arrr:
    print(firstname[i], surname[i], age[i])

sarr = np.searchsorted(arr, 4) # Gives the index where 4 exists or can be inserted to keep order
print(sarr)

parr = np.partition(arr, 4) # Arrange elements so that before the index=4 are smaller or equal to index[4] and after are greater or equal
print(parr)

x = np.array([[1,2],[3,4]])
y = np.array([[5,6]]) # To concatenate, dimensions must match except along the concatenation axis

z = np.concatenate([x,y], axis=0) # Concatenate along rows
z = np.concatenate([x,y.T], axis=1) # Concatenate along columns
print(z)