
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

plt.figure()
fig,ax=plt.subplots(1,2,figsize=(18, 10))

setosa.plot(x="sepal_length", y="sepal_width", kind="scatter",ax=ax[0],label='setosa',color='r')
versicolor.plot(x="sepal_length",y="sepal_width",kind="scatter",ax=ax[0],label='versicolor',color='b')
virginica.plot(x="sepal_length", y="sepal_width", kind="scatter", ax=ax[0], label='virginica', color='g')

setosa.plot(x="petal_length", y="petal_width", kind="scatter",ax=ax[1],label='setosa',color='r')
versicolor.plot(x="petal_length",y="petal_width",kind="scatter",ax=ax[1],label='versicolor',color='b')
virginica.plot(x="petal_length", y="petal_width", kind="scatter", ax=ax[1], label='virginica', color='g')


ax[0].set(title='Sepal comparasion ', ylabel='sepal-width')
ax[1].set(title='Petal Comparasion',  ylabel='petal-width')
ax[0].legend()
ax[1].legend()


plt.figure()
fig,ax=plt.subplots(1,2,figsize=(18, 10))

setosa.plot(x="sepal_length", y=0, kind="scatter",ax=ax[0],label='setosa',color='r')
versicolor.plot(x="sepal_length",y=1,kind="scatter",ax=ax[0],label='versicolor',color='b')
virginica.plot(x="sepal_length", y=2, kind="scatter", ax=ax[0], label='virginica', color='g')


ax[0].set(title='Sepal comparasion ', ylabel='sepal-width')

ax[0].legend()

# plt.show()
# plt.close()
