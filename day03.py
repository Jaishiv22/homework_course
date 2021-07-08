import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

import seaborn as sns 
import pandas as pd
fmri = sns.load_dataset('fmri')
fmri.head()
sns.relplot(data = fmri, x = 'timepoint', y = 'signal', hue = 'region', style = 'event')
plt.show()