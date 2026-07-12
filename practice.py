import pandas as pd
import matplotlib as plt


df = pd.read_csv("netflix_titles.csv")
# explore the data
print(df.head())

print(df.tail())

print(df.describe())

print(df.info())

print(df.isnull().sum())

# data cleaning

df= df.drop_duplicates()
df["country"] = df["country"].fillna("unknown")
df["director"] = df["director"].fillna("not available")

# data analysis

print(df["type"].value_counts())

print(df["country"].value_counts().head(10))

print(df["rating"].value_counts().head(10))

print(df["release_year"].value_counts().sort_index())

print(df["director"].value_counts().head(10))

# filtiering

movies = df[df["type"] == "movie"]
print(movies.head())

tv = df[df["type"] == "ty show"]
print(tv.head())

print(df[df["release_year"] > 2022])

df.to_csv("netflix_cleaned.csv", index=True)