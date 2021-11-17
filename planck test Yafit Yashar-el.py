#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install requests')
import json
import requests


# In[4]:


#api as jason object
response = requests. get('https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod=pickup')
json_data = json. loads(response. text)
#print (json_data)


# In[5]:


#checking objects structure
for item in json_data.get("Data"):
#    print (item)
# i couldn't reach the inside of Data (whrere drinks are) by any query or function


# In[7]:


#jason_str = str(json_data)


# In[8]:


#print(jason_str)


# In[9]:


#search = jason_str.find("drinks")


# In[13]:


object= json_data.get["Data".get("categoriesList")]


# In[ ]:




