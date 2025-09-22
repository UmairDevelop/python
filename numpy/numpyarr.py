import numpy as np
import math

od = np.array([1,2,3,4])
td = np.array([[1,2],[3,4],
               [5,6],[7,8]])
thd = np.array([[[1,2],[3,4],[0,0]], # 4 Blocks of 2d array
                [[5,6],[7,8],[0,0]], # Each 2d array has 3 rows
                [[9,10],[11,12],[0,0]], # Each row has 2 columns
                [[13,14],[15,16],[0,0]]]) # .shape = (4,3,2)

print(od.ndim, td.ndim, thd.ndim) # 1D, 2D, 3D array

print(thd.shape) # Output: (4, 3, 2)
print(td.shape) # Output: (4, 2)
print(od.shape) # Output: (4,)

print(thd.size)  # Total number of elements = 4*3*2 = 24
print(td.size == math.prod(td.shape))

print(od.dtype) # Output: int64 (or int32 depending on the system)