#!/usr/bin/env python
# coding: utf-8

# In[9]:


from kafka import KafkaConsumer
from time import sleep
from json import dumps,loads
import json
from s3fs import S3FileSystem


# In[10]:


consumer = KafkaConsumer(
    'demo_testing2',
     bootstrap_servers=['18.232.129.85:9092'], #add your IP here
    value_deserializer=lambda x: loads(x.decode('utf-8')))


# In[11]:


s3 = S3FileSystem()


# In[12]:


#create an s3 bucket 
for count, i in enumerate(consumer):
    with s3.open("s3://stockmarket-final-data1/stock_market_{}.json".format(count), 'w') as file:  
        json.dump(i.value, file)    


# In[ ]:





# In[ ]:




