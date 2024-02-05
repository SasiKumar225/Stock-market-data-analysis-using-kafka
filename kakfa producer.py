#!/usr/bin/env python
# coding: utf-8

# In[18]:


pip install kafka-python


# In[19]:


import pandas as pd
from kafka import KafkaProducer
from time import sleep
from json import dumps
import json


# In[20]:


producer = KafkaProducer(bootstrap_servers=['18.232.129.85:9092'], #change ip here
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))


# In[21]:


producer.send('demo_kafka', value={"fname":'sasi'})   #demo_kafka is the topic i created in kafka 


# In[22]:


import pandas as pd
pd.set_option('display.max_rows', None)    # To display all rows
pd.set_option('display.max_columns', None)


# In[23]:


df = pd.read_csv("downloads/stockmarketdata.csv")


# In[24]:


df.head(15)


# In[26]:


while True:
    dict_stock = df.sample(1).to_dict(orient="records")[0]
    producer.send('demo_kafka', value=dict_stock)
    sleep(1)


# In[ ]:




