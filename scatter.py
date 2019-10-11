import pandas as pd
import matplotlib.pyplot as plt
from random import shuffle

data = pd.read_csv('~/Downloads/Export201718.csv')
plt.scatter(data.iloc[:, -2], data.iloc[:, -1])
plt.xlabel('EXPORT QUANTITY')
plt.ylabel('EXPORT VALUE in USD')
plt.savefig('/home/stuti/Desktop/Scatter_Plot.png', dpi=300, format='png', bbox_inches='tight')