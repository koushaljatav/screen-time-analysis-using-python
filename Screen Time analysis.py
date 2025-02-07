#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


# In[2]:


data=pd.read_csv('Screentime-App-Details-Dataset.csv')


# In[3]:


data.head(10)


# In[4]:


data.isnull()


# In[5]:


data.isnull().sum()


# In[6]:


data.describe()


# In[7]:


figure=px.bar(data_frame=data,x="Date",y="Usage",color="App",title="usage graph by koushal jatav")
figure.show()


# In[8]:


figure=px.bar(data_frame=data,x="Date",y="Notifications",color="App",title="Notifications graph by koushal jatav")
figure.show()


# In[9]:


figure=px.bar(data_frame=data,x="Date",y="Times opened",color="App",title="Times opened graph by koushal jatav")
figure.show()


# In[10]:


figure=px.scatter(data_frame=data,x="Notifications",y="Usage",
size="Notifications",trendline="ols",title="Relationship between  no. of notification and amount of usage ")
figure.show()


# In[ ]:




