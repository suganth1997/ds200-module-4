import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from random import shuffle

data = pd.read_csv('./Export201718.csv')
value = data.iloc[:, -1][:-1] #Last Vlaue was a outlier
plt.boxplot(value)
plt.yscale('log')
plt.ylabel('Export Value in USD')
plt.grid()
plt.savefig('Box_Plot.png', dpi=300, format='png', bbox_inches='tight')
