
import pandas as pd
from kafka import KafkaProducer
from time import sleep
from json import dumps
import json


producer = KafkaProducer(bootstrap_servers=['18.232.129.85:9092'], #change ip here
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))


producer.send('demo_kafka', value={"fname":'sasi'})   #demo_kafka is the topic i created in kafka 

import pandas as pd
pd.set_option('display.max_rows', None)    # To display all rows
pd.set_option('display.max_columns', None)


df = pd.read_csv("downloads/stockmarketdata.csv")
df.head(15)
while True:
    dict_stock = df.sample(1).to_dict(orient="records")[0]
    producer.send('demo_kafka', value=dict_stock)
    sleep(1)
