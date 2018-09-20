#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import inline as inline

get_ipython().run_line_magic('matplotlib', 'inline')


pd.set_option('display.width', 400)
pd.set_option('display.max_columns', 23)
pd.set_option('display.max_rows', 100)

pd.options.mode.chained_assignment = None

plt.style.use('default') # haciendo los graficos un poco mas bonitos en matplotlib
#plt.rcParams['figure.figsize'] = (20, 10)

sns.set(style="whitegrid") # seteando tipo de grid en seaborn

df = pd.read_csv('events.csv')


# In[7]:


df


# In[50]:


df_model = df[df.model.notnull()][['person', 'model']]
model_persons = df_model['person']                #  SERIE CON PERSONAS QEUE ESTA
df_model_users = df.loc[df['person'].isin(model_persons), :]
df_model_users_buys = df_model_users.loc[df['event'] == 'conversion']
models_counts = df_model_users_buys['model'].value_counts()
models_counts


# In[63]:


sales_Samsung = sum(df_model_users_buys['model'].loc[df_model_users_buys['model'].str.contains('Samsung')].value_counts())
sales_iPhone = sum(df_model_users_buys['model'].loc[df_model_users_buys['model'].str.contains('iPhone')].value_counts())
sales_Motorola = sum(df_model_users_buys['model'].loc[df_model_users_buys['model'].str.contains('Motorola')].value_counts())
sales_LG = sum(df_model_users_buys['model'].loc[df_model_users_buys['model'].str.contains('LG')].value_counts())
sales_Sony = sum(df_model_users_buys['model'].loc[df_model_users_buys['model'].str.contains('Sony')].value_counts())
sales_Asus = sum(df_model_users_buys['model'].loc[df_model_users_buys['model'].str.contains('Asus')].value_counts())
sales_Lenovo = sum(df_model_users_buys['model'].loc[df_model_users_buys['model'].str.contains('Lenovo')].value_counts())

df_brand_sales = pd.DataFrame({'brand': ['Samsung', 'iPhone', 'Motorola', 'LG', 'Sony', 'Asus', 'Lenovo'],
                   'sales': [sales_Samsung, sales_iPhone, sales_Motorola, sales_LG, sales_Sony, sales_Asus, sales_Lenovo]})
df_brand_sales


# In[67]:


sales_Samsung = df_model_users_buys['model'].loc[df_model_users_buys['model'].str.contains('Samsung')].value_counts().head(15)

g2 = sns.barplot(x=sales_Samsung.index, y=sales_Samsung.values, orient = 'v')
plt.xticks(rotation=90)
g2.set_title("Samsung model sales", fontsize = 15)
g2.set_xlabel("Model", fontsize = 12)
g2.set_ylabel("Frequency", fontsize = 12)


# In[68]:


sales_iPhone = df_model_users_buys['model'].loc[df_model_users_buys['model'].str.contains('iPhone')].value_counts().head(15)

g2 = sns.barplot(x=sales_iPhone.index, y=sales_iPhone.values, orient = 'v')
plt.xticks(rotation=90)
g2.set_title("Samsung model sales", fontsize = 15)
g2.set_xlabel("Model", fontsize = 12)
g2.set_ylabel("Frequency", fontsize = 12)


# In[72]:


df_releaseYear_model = pd.DataFrame({'model': ['Samsung Galaxy J5', 'iPhone 5s', 'Motorola'],
                   'releaseYear': [2017, 2013, 2016]})
df_releaseYear_model


# In[71]:


sales_Motorola = df_model_users_buys['model'].loc[df_model_users_buys['model'].str.contains('Motorola')].value_counts().head(15)

g2 = sns.barplot(x=sales_Motorola.index, y=sales_Motorola.values, orient = 'v')
plt.xticks(rotation=90)
g2.set_title("Samsung model sales", fontsize = 15)
g2.set_xlabel("Model", fontsize = 12)
g2.set_ylabel("Frequency", fontsize = 12)

