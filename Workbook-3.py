#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


import numpy as np 


# In[6]:


x = np.linspace(0,5,11)
y = x**2


# In[7]:


x


# In[8]:


y


# In[9]:


#Functional Method 


# In[11]:


plt.plot(x,y)
plt.xlabel("X Label")
plt.ylabel("Y Label")
plt.title("Title")


# In[12]:


plt.subplot(1,2,1)
plt.plot(x,y,"r")


plt.subplot(1,2,2)
plt.plot(y,x,"b")


# In[13]:


#Object Oriented Method 


# In[18]:


fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])
axes.plot(x,y)
axes.set_xlabel("X Label")
axes.set_ylabel("Y Label")
axes.set_title("Set Title")


# In[30]:


fig = plt.figure()
axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
axes2 = fig.add_axes([0.15,0.4,0.5,0.5])


# In[37]:


fig, axes = plt.subplots(nrows = 1, ncols = 2)
#axes.plot(x,y)


# In[47]:


fig,axes = plt.subplots(nrows = 2, ncols = 1, figsize = (5,5))


axes[0].plot(x,y)
axes[1].plot(y,x)

plt.tight_layout()


# In[48]:


fig.savefig("my_picture.png")


# In[59]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,x**2, label = "X Square")
ax.plot(x,x**3, label = "X Cubed")
ax.set_xlabel("X label")
ax.set_ylabel("Y label")
ax.set_title("Title")
ax.legend(loc = 0)


# In[93]:


fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y,color = "purple", lw = 1, alpha = 1, ls = "-", marker = "+")


# In[84]:


x


# In[85]:


len(x)


# In[ ]:




