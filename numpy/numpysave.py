import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9,10])
np.save('saved_sample_array.npy', a)

b = np.load('saved_sample_array.npy')
print(b)

# arr = np.arange(10,50,3,dtype=int).reshape(2,7)
arr = np.random.randint(10,50,(3,3))
np.savetxt('saved_sample_csv.csv', arr, delimiter=',') # Saves as CSV file
b = np.loadtxt('saved_sample_csv.csv', dtype=float) 
b = b.astype(int)
print(b)