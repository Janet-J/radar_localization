import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


x= np.linspace(0,10,100)
''''
print(x[:10])
fig, ax = plt.subplots()
print(ax.hist(x,x**2))
#plt.show()

y= pd.date_range('1/1/2020', periods=10)
print(y)

heart_disease= pd.read_csv('heart-disease.csv')
print(heart_disease.head())
heart_disease['age'].plot.hist(bins=50)
plt.show()

heart_disease.plot.hist(subplots=True)
plt.show()

'''
'''
fig,((a1,a2),(a3,a4))=plt.subplots(2,2, figsize=(10,8))
a1.plot(x,x)
a2.plot(x,x**2)
a3.plot(x,x)
a4.plot(x,x**2)
plt.tight_layout()
plt.show()
'''


heart_disease=pd.read_csv('heart-disease.csv')
print(heart_disease.head())
#heart_disease.plot.hist(subplots=True, figsize= (20,50))
plt.show()
fig,ax=plt.subplots()
heart_disease['age']=heart_disease['age'].astype(int)
heart_disease['target']=heart_disease['target'].astype(int)
print(heart_disease['target'].dtypes)
ax.plot(heart_disease['age'],heart_disease['target'])
#plt.show()

#oo method from scratch
over_50=heart_disease[heart_disease['age']>50]
fig,(ax1,ax2)= plt.subplots(nrows=2,
                            ncols=1,
                            figsize=(10,6)
                            )
scatter = ax1.scatter(x=over_50['age'],
                     y=over_50['chol'],
                     c=over_50['target']
                     )
ax1.set(title='Heart disease and cholestrol levels', 
       xlabel='age,',
       ylabel='cholestrol')
ax1.legend(*scatter.legend_elements(), title='Target')
scatter=ax2.scatter(x=over_50['age'],
                     y=over_50['chol'],
                     c=over_50['target']
                     )
ax2.set(title='heart disese',
        xlabel='Age',
        ylabel='Cholestrol')
ax2.legend(*scatter.legend_elements(), title='Target')
fig.suptitle('Heart disease', fontsize='16')

plt.show()
plt.style.available()