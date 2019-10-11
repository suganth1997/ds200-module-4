import pandas as pd
import matplotlib.pyplot as plt
from random import shuffle

data = pd.read_csv('~/Downloads/Export201718.csv')
qty_group = data.groupby('COMMODITY')['QTY'].sum()
qty_group = qty_group.sort_values(ascending = False)
top30 = qty_group[:30]
shuffle(top30)
plt.bar(top30.index, top30)
plt.xticks(rotation = 90)
plt.ylabel('EXPORT QUANTITY')
plt.savefig('/home/stuti/Desktop/Bar_Plot.png', dpi=300, format='png', bbox_inches='tight')