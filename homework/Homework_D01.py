#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# In[4]:


np.__version__


# In[5]:


array=np.arange(1,21,1)


# In[6]:


array


# In[7]:


Aws2=array %2==0


# In[8]:


Aws2


# In[10]:


array[Aws2]


# In[11]:


Aws3=array%3==0


# In[12]:


Aws3


# In[13]:


array[Aws3]


# In[ ]:




