import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as sk
import graphlab as gl

data = pd.read_csv("train.csv")
print("Data Read")
new = {}
for i in range(111):
    new[data.columns.values[i]] = int(str(data[[i]].isnull().sum()).split()[1])

print("Dictionary Made")
plt.bar(range(len(new)), new.values(), align='center')
plt.xticks(range(len(new)), new.keys())
plt.show()