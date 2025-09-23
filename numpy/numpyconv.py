import numpy as np

od = np.array([1,2,3,4,5,6])
td = od[np.newaxis, :] # Row vector
thd = td[:, np.newaxis] # Column vector

print(td.ndim)
print(td)
print(thd.shape)
print(thd)

na = np.array([1,2,3,4,5,6,7,8]) 
na = np.expand_dims(na, axis=0) # 
print(na.shape)
print(na)