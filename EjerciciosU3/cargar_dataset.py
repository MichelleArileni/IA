import seaborn as sns
import matplotlib.pyplot as plt
sns.set(color_codes=True)
import pandas as pd

dataset = pd.read_csv('C:/Users/Michelle/Desktop/Itsur/Semestre 8/I. Artificial/IAiris.csv')
dataset.head()

print(dataset.shape)
print(dataset.info())
print(dataset.describe())
print(dataset.groupby('species').size())

from pandas.plotting import scatter_matrix
sns.pairplot(dataset, hue="species")

setosa=dataset[dataset['species']=='setosa']
versicolor =dataset[dataset['species']=='versicolor']
virginica =dataset[dataset['species']=='virginica']

print(setosa.describe())
print(versicolor.describe())
print(virginica.describe())