#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


df = pd.read_csv("train.csv")


# In[4]:


df.head()


# In[5]:


df.info()


# In[6]:


df.describe()


# In[7]:


df


# In[8]:


# Drop rows with missing values
df.dropna(inplace=True)


# In[9]:


# Handle Duplicates
df.drop_duplicates(inplace=True)


# In[10]:


#Save Cleaned Data
df.to_csv('cleaned_data.csv', index=False)


# In[ ]:




