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
# print(df2)
# print(df2.dtypes) # Shows the data types of cloumns in dataframe
# print(df2.head(2)) # Gives the first 2 rows of dataframe
# print(df2.tail(1), "\n\n") # Gives one bottom end row

array = df2.to_numpy() # Converts to numpy array
# print(array.dtype) # Numpy array can store only one data type whereas dataframe can store one data type per column so on conversion the array gets the compatible datatype that can hold it
# print(df2.describe()) # Gives a predefined summary of dataframe

# print(df2.sort_index(axis=1, ascending=False)) # Column reverse
# print(df2.sort_values(by="B"))

#print(df["A"])
#print(df[0:3])
#print(df["20130102":"20130104"])

#print(df.loc[date_range[1]]) # Select only one row from the dataframe
#print(df.loc[:,["A","B"]]) # Select all rows :, but columns A and B
#print(df.loc["20130103":"20130106", ["A","B"]]) # Select only in betweeen the give data 
#print(df.loc[date_range[0],"A"]) # Selecting like this only gives a single value
#print(df.at[date_range[0], "A"]) # Same like above but gives fast access and it only works on single values
# print(df.iloc[3]) # Select by position or index
# print(df.iloc[2:4,1:3]) # Slicing similar to numpy 
# print(df.iloc[[1,2,4],[0,3]]) # Selects only the given indices/indexes
# print(df.iloc[1:3, :])
# print(df.iloc[:, 1:3])
# print(df.iloc[1,1])
# print(df.iat[1,2])

# print(df[df["A"] > 0]) # Boolean Selection
# print(df[df > 0])

df3 = df.copy()
df3["F"] = ["One", "Two", "Three", "Four", "Five", "Six"]
# print(df3)
# print(df3[df3["F"].isin(["Two", "Three"])]) # Selection using isin method by using the given keys

# s1 = pd.Series([1,2,3,4,5,6], pd.date_range("20130102", periods=6))
# df["F"] = s1
# df.at[date_range[0], "A"] = 0 # Setting values by Label
# df.iat[0,4] = 0 # Setting value using index or position
# df.loc[:,["E"]] = np.array([5] * len(df)) 

cdf = df.copy()
cdf[cdf > 0] = -cdf # Applies negative to evry value greater than zero

rdf = df.reindex(index=date_range[0:4], columns=list(df.columns) + ["F"])
rdf.loc[date_range[0]:date_range[1], "F"] = 1
# rdf.iloc[0:2, 6] = 1
print(rdf.dropna(how="any")) # Drop the nan in the dataframe
# rdf = rdf.fillna(value=5) # Replace the nan with the give value 
print(pd.isna(rdf)) # Shows which vlue in a dataframe is nan in boolean values
