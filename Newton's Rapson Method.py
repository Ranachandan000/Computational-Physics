#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


def newtonsmethod(func,df,x,iteration):
    for i in range(iteration):
        x -= func(x)/df(x)
    return x


# In[3]:


def func(x):
    return x**2 -2


# In[5]:


def df(x):
    return 2*x


# In[6]:


newtonsmethod(func,df,2,10)


# In[ ]:




