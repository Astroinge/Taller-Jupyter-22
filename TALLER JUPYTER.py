#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import matplotlib.pyplot as plt


# In[10]:


listAltura = (1.88, 1.60, 1.60, 1.60, 1.60, 1.60, 1.65), (1.59, 1.75, 1.59, 1.72, 1.74, 1.80, 1.69)
altura = np.array (listAltura)
altura


# In[11]:


media= np.mean(altura)
media


# In[12]:


mediana = np.median(altura)
mediana


# In[13]:


desviacion = np.std(altura)
desviacion


# In[20]:


plt.imshow(altura, cmap= "plasma")
plt.colorbar(label = "Altura en metros")
plt.show

