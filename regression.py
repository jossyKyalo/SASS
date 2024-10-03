import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("data.csv")
print(df.head())
print(df.info())
print(df.describe())
print(df[['Quantity', 'UnitPrice']].isnull().sum())  
#EDA

print(sns.jointplot(x="Quantity", y="UnitPrice", data=df))
plt.show()