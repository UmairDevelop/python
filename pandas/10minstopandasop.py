import numpy as np
import pandas as pd

dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list("ABCD"))

# print(df.mean()) # Calculate the mean of each column
# print(df.mean(axis=1)) #Calculates the mean of each row

s = pd.Series([1,2,3,4,np.nan,5], index=dates).shift(2) # Shift moves down 2 rows
df.sub(s, axis="index") # Sub means subtract and axis="index" mean rows when passed s with the axis index it will subtract the rows with df since first two in s was nan it will make the the first 2 rows in df nan

df.transform(lambda x: x * 101.5) # Transform can take a user defined function mostly to broadcast df.agg works the same way

s = pd.Series(np.random.randint(0,7,size=10))
s.value_counts()

string = pd.Series(["A", "B", "C", "ab", "abc", "Aaba", "Baba", np.nan, "dog", "cat"])
string.str.lower()
string.str.replace("dog", "fish")

df = pd.DataFrame(np.random.randn(10,4))
pieces = [df[:3], df[3:7], df[7:]]
pd.concat(pieces) # Conmine the pieces together

left = pd.DataFrame({"key" : ["foo", "foo"], "lval" : [1,2]})
right = pd.DataFrame({"key" : ["foo", "foo"], "rval" : [3,4]})
mrg = pd.merge(left, right, on="key") # Merge both rows and columns in order on common key: foo 1 3 -> foo 1 4 -> foo 2 3 -> foo 2 4

left = pd.DataFrame({"key": ["foo", "bar"], "lval" : [1,2]})
right = pd.DataFrame({"key": ["foo", "bar"], "rval" : [3,4]})
uni_mrg = pd.merge(left, right, on="key") # Merge on unique key: foo 1 3 -> bar 2 4

df = pd.DataFrame({
    "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
    "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
    "C": np.random.randn(8),
    "D": np.random.randn(8),
})
df.groupby("A")[["C", "D"]].sum() # Group based on column A select the unique keys from A and shows only those unique key rows
df.groupby(["A", "B"]).sum() # Group based on two columns A and B selects the unique values and combine them 

arrays = [
    ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
    ["one", "two", "one", "two", "one", "two", "one", "two"],
]
index = pd.MultiIndex.from_arrays(arrays, names=["First", "Second"]) # For creating a hirearchy in dataframe 
df = pd.DataFrame(np.random.randn(8,2), index=index, columns=["A", "B"]) # First will be A and B then First and Second 

stacked = df.stack(future_stack=True) # Converts the Column into row 
stacked = stacked.unstack() # Reverse the stack operation
stacked = stacked.unstack(0) # Converts the column into row based on the index

df = pd.DataFrame({
    "A": ["one", "one", "two", "three"] * 3,
    "B": ["A", "B", "C"] * 4,
    "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
    "D": np.random.randn(12),
    "E": np.random.randn(12),
})

pivot_t = pd.pivot_table(df, values=["D"], index=["A", "B"], columns=["C"]) # Pivots the table based on the order provided 

rng = pd.date_range("1/1/2012", periods=100, freq="s")
tf = pd.Series(np.random.randint(0, 500, len(rng)), index=rng) 
tf.resample("5min").sum() # Adds up all the random number in the frequency of 5 mins

rng = pd.date_range("1/1/2012 00:00", periods=5, freq="D")
tf = pd.Series(np.random.randn(len(rng)), rng)
ts_utc = tf.tz_localize("UTC")
ts_utc = ts_utc.tz_convert("US/Eastern")

rng = rng + pd.offsets.BusinessDay(5) # Adds 5 business days to rng 


df = pd.DataFrame({
    "id": [1,2,3,4,5,6],
    "raw_grade": ["a","b","b","a","a","e"],
})
df["grades"] = df["raw_grade"].astype("category")
new_categories = ["very good", "good", "very bad"]
df["grades"] = df["grades"].cat.rename_categories(new_categories) # Renames the categories
df["grades"] = df["grades"].cat.set_categories([
    "very bad", "bad", "medium", "good", "very good"
])
df.sort_values(by="grades") # Sort 
df.groupby("grades", observed=False).size() # Gives the count of values against each category
df.to_csv("sample.csv")  
df2 = pd.read_csv("imdb_train.csv")