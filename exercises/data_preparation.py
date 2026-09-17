import pandas as pd
from sklearn.preprocessing import MinMaxScaler

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
column_names = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
df = pd.read_csv(url, names=column_names)

array = df.values
X = array[:, 0:8]
Y = array[:, 8]

scaler = MinMaxScaler(feature_range=(0, 1))
X_scaled = scaler.fit_transform(X)

print("Before scaling (first row):", X[0])
print("After scaling (first row):", X_scaled[0])


from sklearn.preprocessing import StandardScaler

standardizer = StandardScaler()
X_standardized = standardizer.fit_transform(X)

print("Before standardization (first row):", X[0])
print("After standardization (first row):", X_standardized[0])