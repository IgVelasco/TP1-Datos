# importacion general de librerias y de visualizacion (matplotlib y seaborn)
import inline as inline
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

desired_width=400

pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 23)
pd.set_option('display.max_rows', 100)


plt.style.use('default') # haciendo los graficos un poco mas bonitos en matplotlib
#plt.rcParams['figure.figsize'] = (20, 10)

sns.set(style="whitegrid") # seteando tipo de grid en seaborn

pd.options.display.float_format = '{:20,.2f}'.format # suprimimos la notacion cientifica en los outputs

import warnings
warnings.filterwarnings('ignore')

# %timeit sirve para evaluar el tiempo de ejecucion
df = pd.read_csv('events.csv')
df_campaign = df[df.campaign_source.notnull()]
campaign_persons = df_campaign['person']
df_campaign_users = df.loc[df['person'].isin(campaign_persons), :]




print(df_campaign_users.shape)
print(df_campaign.shape)

#df_null = df[df.model.isnull()]

#print(df_null.shape)





