#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd

df = pd.read_csv('YEMEN.csv')
df['sub_event_type'] = df['sub_event_type'].str.replace('\W', '_')


# In[6]:


df['sub_event_type'].unique()


# In[7]:


for i, g in df.groupby('sub_event_type'):
    g.to_csv('{}.csv'.format(i), header=True)


# In[ ]:




