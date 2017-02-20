
# coding: utf-8

# # Latitude and Longitude of any location
# 
# Just Enter the location and the latitude and longitude will be displayed.

# In[50]:

print("Enter the address")
address = input()
url = "https://maps.googleapis.com/maps/api/geocode/json?address="+address+"&key=AIzaSyCGcI8jCP6rw0mAIUIZKBgyonpFifXq0z4"


# In[51]:

import requests

r = requests.get(url)


# In[52]:

results = r.json()
results


# In[53]:

geometry = results["results"][0]["geometry"]
lat = geometry["location"]["lat"]
long = geometry["location"]["lng"]


# In[54]:

print("Latitude {}".format(lat))
print("Longitude {}".format(long))


# In[ ]:



