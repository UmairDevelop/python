import numpy as np
import pandas as pd

df = pd.read_csv("imdb_train.csv")
#df.info() # Gives the information about the dataframe

# Show the first 10 rows of the dataset.
df.head(10)
df[:10]

# Check the shape (rows & columns).
df.shape
print(f"Rows: {df.shape[0]} Columns: {df.shape[1]}")

# Get a list of all column names.
df.columns
df.columns.tolist()

# Find the number of missing values in each column.
df.isnull().sum()
#df.info()

# Get summary statistics (mean, min, max, count) for numeric columns.
df.describe()

# Select only one column and turn it into a Series.
ser = pd.Series(df["review"])

# Select two specific columns and make a new DataFrame.
df2 = pd.DataFrame(df[["review", "label"]])

# Sort the DataFrame by a numeric column in descending order.
df_sorted = df.sort_values(by="label", ascending=False)
df_sorted["label"]

# Filter rows where a column’s value is greater than a threshold.
df_greater_than_zero = df[df["label"] > 0]
df_greater_than_zero["label"]

# Count how many times each unique value appears in a categorical column
df["review"].value_counts()
df.value_counts("review")

# Replace missing values in a column with the column’s mean.
df["label"].fillna(df["label"].mean(), inplace=True)

# Add a new column that is a calculation of two other columns (e.g., ratio)
df["combi"] = df["review"] + df["label"].astype(str)
df["combi"].head(2)

# Rename a column.
df.rename(columns={"combi": "combined"}, inplace=True)
df.columns

# Drop rows with missing values.
df.dropna()

# Save the cleaned dataset as a CSV.
df.to_csv("imdb_train_modified.csv")