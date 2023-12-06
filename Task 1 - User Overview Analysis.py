#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings 
warnings.filterwarnings('ignore')


# In[2]:


df = pd.read_excel('telcom_data.xlsx')
df.head()


# In[3]:


df.shape


# In[4]:


df.info()


# In[5]:


df.columns


# In[6]:


df.describe()


# # Data Cleaning and Preprossing

# ### 1. Finding the Null values

# In[7]:


df.isnull().sum()


# In[10]:


df.isnull().sum() * 100


# In[12]:


def percent_missing(df):

  # calculate total number of cells in the dataframe
  totalCells = np.product(df.shape)

  #count the number of missing values per column
  missingCount = df.isnull().sum()

  #calculate the total number of missing valies
  totalMissing = missingCount.sum()

  # calculate the percentage of the missing values
  print("Telecom Dataset contains ", round(((totalMissing/totalCells) * 100), 2), "%", "Missing Values.")

percent_missing(df)


# # Finding the Missing Values

# In[14]:


df.isnull().sum()


# ### Filling missing Values with ffill method for columns ()

# In[17]:


df_missing = df.fillna(df.mean(numeric_only=None))
df_missing
    


# In[18]:


df_missing.isnull().sum()


# In[19]:


columns_fill = ['Last Location Name', 'Handset Manufacturer', 'Handset Type'] 
df_missing[columns_fill] = df_missing[columns_fill].fillna(df_missing[columns_fill].mode().iloc[0])
df_missing


# In[20]:


df_missing.isnull().sum()


# In[21]:


df_missing = df.dropna()
df_missing


# In[22]:


df_missing.isnull().sum()


# In[27]:


clean_df = df_missing
clean_df


# In[23]:


df['Handset Type'].unique()


# # Identifying the top 10 handsets used by the customers

# In[24]:


df1 = df['Handset Type'].value_counts().nlargest(10)
df1 = pd.DataFrame(df1)
df1


# # Identify the top 3 handset manufacturers

# In[25]:


df2 = df['Handset Manufacturer'].value_counts().nlargest(3)
df2 = pd.DataFrame(df2)
df2


# # Identify the top 5 handsets per top 3 handset manufacturer

# In[26]:


# Calculate the total usage for each handset model
handset_usage = df.groupby(['Handset Manufacturer', 'Handset Type']).size().reset_index(name='Total_Usage')

# Find the top 3 handset manufacturers
top_manufacturers = handset_usage.groupby('Handset Manufacturer')['Total_Usage'].sum().nlargest(3).index

# Filter the data for the top 3 manufacturers
top_manufacturer_data = handset_usage[handset_usage['Handset Manufacturer'].isin(top_manufacturers)]

# Identify the top 5 handsets per top 3 manufacturers
top_5_handsets_per_manufacturer = top_manufacturer_data.groupby('Handset Manufacturer').apply(lambda x: x.nlargest(5, 'Total_Usage')).reset_index(drop=True)

# Display the result
print(top_5_handsets_per_manufacturer)


# In[28]:


df2 = clean_df.select_dtypes(include=["float64", "int64"])
df2


# In[29]:


pd.to_numeric(df['IMSI'])


# In[30]:


clean_df['Bearer Id'].value_counts()


# ### Aggregated number of xDR sessions per User(International Mobile Subscriber Identity)
# 

# In[31]:


clean_df.groupby('IMSI').agg({'Bearer Id': 'count'})


# In[32]:


clean_df['Dur. (ms)'].aggregate('sum')


# ### Aggregated number of Session duration per User

# In[33]:


clean_df.groupby('IMSI').agg({'Dur. (ms)': 'count'})


# In[34]:


clean_df['Total DL (Bytes)'].value_counts()


# ### Aggregated total download (DL) and upload (UL) data per User

# In[35]:


clean_df.groupby('IMSI').agg({'Total DL (Bytes)': 'count'})


# In[36]:


clean_df.groupby('IMSI').agg({'Total DL (Bytes)': 'count'})


# In[37]:


clean_df.groupby('IMSI').agg({'Total UL (Bytes)': 'count'})


# ### The total data volume (in Bytes) during this session for each application

# In[38]:


#Social Media
Soc_Med = df['Social Media DL (Bytes)'].aggregate('sum') + df['Social Media UL (Bytes)'].aggregate('sum')
Soc_Med


# In[39]:


#Google
Google = df['Google DL (Bytes)'].aggregate('sum') + df['Google UL (Bytes)'].aggregate('sum')
Google


# In[40]:


#Youtube
Y_tube = df['Youtube DL (Bytes)'].aggregate('sum') + df['Youtube UL (Bytes)'].aggregate('sum')
Y_tube


# In[41]:


#Netflix
Netflix = df['Netflix DL (Bytes)'].aggregate('sum') + df['Netflix UL (Bytes)'].aggregate('sum')
Netflix


# In[42]:


#Gaming
Game = df['Gaming DL (Bytes)'].aggregate('sum') + df['Gaming UL (Bytes)'].aggregate('sum')
Game


# In[43]:


#Other
Other = df['Other DL (Bytes)'].aggregate('sum') + df['Other UL (Bytes)'].aggregate('sum')
Other


# In[ ]:




