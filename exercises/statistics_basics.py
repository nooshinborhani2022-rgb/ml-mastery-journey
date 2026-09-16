import numpy as np

scores = [70, 80, 90, 60, 100]

manual_mean = sum(scores) / len(scores)
numpy_mean = np.mean(scores)

print("Manual mean:", manual_mean)
print("NumPy mean:", numpy_mean)


scores_with_outlier = [70, 80, 90, 60, 1000]

mean_value = np.mean(scores_with_outlier)
median_value = np.median(scores_with_outlier)

print("Mean:", mean_value)
print("Median:", median_value)


class_a = [78, 79, 80, 81, 82]
class_b = [20, 50, 80, 110, 140]

print("Class A - variance:", np.var(class_a), "std:", np.std(class_a))
print("Class B - variance:", np.var(class_b), "std:", np.std(class_b))

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

correlation = np.corrcoef(x, y)[0, 1]
print("Correlation:", correlation)


import pandas as pd

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
column_names = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]
df = pd.read_csv(url, names=column_names)

correlation = df["age"].corr(df["plas"])
print("Correlation between age and glucose:", correlation)