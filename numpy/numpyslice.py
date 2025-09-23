import numpy as np

arr = np.array([1,2,4,6,3,2,6,8,9])
print(arr[1])
print(arr[0:4]) # Slicing: 0 to 3 index
print(arr[:3]) # Slicing: start to 2 index
print(arr[3:]) # Slicing: 3 index to end
print(arr[-4:]) # Slicing: last 4 elements

print(arr[arr > 3]) # Conditional slicing
print(arr[arr%2 == 0]) # Even numbers
print(arr[arr%2 != 0]) # Odd numbers
print(arr[(arr > 2 ) & (arr < 7)]) # Between 2 and 7

barr = np.nonzero(arr < 5) # Gives the indexes where elements are less than 5
print(barr) 

list_of_indexes = list(zip(*barr)) # Converts array of tuples(barr) to list of tuples(barr)
for i in list_of_indexes:
    print(i) # Prints each index of elements less than 5

print(arr[barr]) # Prints elements less than 5 using the indexes in barr

print(np.nonzero(arr == 42)) # If no element matches the condition, it returns an empty array