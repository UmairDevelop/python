import numpy as np
import pandas as pd

seri = pd.Series([1,2,3,4,np.ones((2,2)),5,6,7], name="random") # Series is like a 1D array
rindex = np.array([pd.RangeIndex(5)]) # Generates values till 5 not including 5 : 0,1,2,3,4
strindex = list(pd.RangeIndex(0,10,2)) # Generates values till 10 with the step of 2 not including 10: 0,2,4,6,8
trindex = np.array([[pd.RangeIndex(2,-10,-3)]]) # Starts from 2 and goes back till -10 with 3 steps not including -10
# print(seri)
# print(rindex)
# print(strindex)
# print(trindex)

date_range = pd.date_range("20130101", periods=6) # For Dates and the period is the amount of days period=6 == days=6 
df = pd.DataFrame(np.random.randn(6,5), index=date_range, columns=list("ABCDE")) # The value to randn is set to 6,5 because 6 is the number of rows that we set like date from 01-06 and 5 is the nummber of columns in the dataframe that we specified "ABCDE"
print(df, "\n")
print(df.index, "\n")
print(df.columns, "\n")


data = { # Dicitionary with different data types
    "A": 1.0,
    "B": pd.date_range("20140101", periods=4),
    "C": pd.Series(1, index=list(range(4)), dtype=float), # Creates a series of 1 with range 4 : 1.0, 1.0, 1.0, 1.0
    "D": np.array([3] * 4, dtype="int32"), 
    "E": pd.Categorical(["test", "train", "test", "train"]), # Create categorys 
    "F": "foo", # Object 
}
df2 = pd.DataFrame(data)
print(df2)
print(df2.dtypes) # Shows the data types of cloumns in dataframe
print(df2.head(2)) # Gives the first 2 rows of dataframe
print(df2.tail(1), "\n\n") # Gives one bottom end row

array = df2.to_numpy() # Converts to numpy array
print(array)