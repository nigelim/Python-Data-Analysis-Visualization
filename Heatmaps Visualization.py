import numpy as np
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas import Series, DataFrame

df = sns.load_dataset('flights') #-> Dataset from GitHub
df2 = df.pivot('year','month','passengers') #-> Pivot table of: 'rows,'columns','passengers'
print(df2)

#Heatmap
plt.clf()
sns.heatmap(df2).get_figure().savefig('heatmap1.png')
#annot, fmt
plt.clf()
sns.heatmap(df2,annot=True,fmt='d').get_figure().savefig('heatmap2.png')
#.loc
plt.clf()
sns.heatmap(df2, center=df2.loc[1955,'Jan']).get_figure().savefig('heatmap3.png')
#-> the center location was deemed as 1955, Jan. The colors above and below it will be of a different color.
#Useful for scenarios such as the breakeven points of a business between loss and profit.