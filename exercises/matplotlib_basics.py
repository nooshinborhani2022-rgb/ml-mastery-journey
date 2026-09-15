import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
column_names = ["preg", "plas", "pres", "skin", "test", "mass", "pedi", "age", "class"]

df = pd.read_csv(url, names=column_names)

df["age"].hist()
plt.title("Age distribution")
plt.xlabel("Age")
plt.ylabel("Number of people")
plt.show()


plt.scatter(df["age"], df["plas"], c=df["class"])
plt.title("Age vs Glucose (colored by diabetes)")
plt.xlabel("Age")
plt.ylabel("Plasma glucose")
plt.show()