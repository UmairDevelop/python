from datasets import load_dataset

ds = load_dataset("ajaykarthick/imdb-movie-reviews")
print(ds["train"])
with open("imdb_train.csv", 'w', newline='') as f:
    csv = ds["train"].to_csv("imdb_train.csv")