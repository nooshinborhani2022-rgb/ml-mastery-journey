import pandas as pd

data = {
    "name": ["Ali", "Sara", "Reza"],
    "age": [23, 31, 27],
    "score": [85, 92, 76]
}

df = pd.DataFrame(data)

print(df)
print("Shape:", df.shape)
print("Column names:", df.columns)

# Access a single column by name
print("Ages:", df["age"])

# Quick statistical summary
print(df.describe())


url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
column_names = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]

df2 = pd.read_csv(url, names=column_names)

print(df2.head())
print("Shape:", df2.shape)


array = df2.values  # convert DataFrame to a NumPy array

X = array[:, 0:8]
Y = array[:, 8]

print("X shape:", X.shape)
print("Y shape:", Y.shape)