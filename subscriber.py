import io
import operator
from PIL import Image, UnidentifiedImageError
import PIL
from matplotlib import pyplot as plt
from io import BytesIO
import json
from kafka import KafkaConsumer
import base64
import numpy as np
consumer = KafkaConsumer(
        'jumat',
        bootstrap_servers='192.168.254.135:9092',api_version=(0,10,1),
        max_partition_fetch_bytes=10485760,
        auto_offset_reset='latest')
        #earliest
for message in consumer:
    a=json.loads(message.value)
    print(a)
    sending=a[1]
    #data1=a[1]
    #data2=a[2]
    #sending=data1+data2
    receive=sending
    print(receive)
    print(type(receive))
    with open("jabar_new.jpg", "wb") as new_file:
        decoded=new_file.write(base64.b64decode(receive))
    print("decoded:",decoded)
    print(type(decoded))


