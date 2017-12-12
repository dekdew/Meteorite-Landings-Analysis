import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')
data = data[(data.reclat != 0) & (data.reclong != 0)]
data.info()

valt = data.groupby('nametype').get_group('Valid').copy()
valt.dropna(inplace=True)
valt.info()

plt.scatter(valt.year,valt.reclat,color='g',alpha=0.4)
plt.xlim(1900,2013)
plt.ylim(-90,90)
plt.ylabel('Latitude')
plt.xlabel('Year')
plt.title('Meteorite recorded latitude vs year')
plt.show()