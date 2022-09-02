import cv2
import numpy as np
import matplotlib.pyplot as plt
from random import randrange, getrandbits
import os
from kafka import KafkaProducer
import json
import io
import base64
from PIL import Image, UnidentifiedImageError
import PIL
def serializer(message):
    return json.dumps(message).encode('utf-8')
producer=KafkaProducer(bootstrap_servers=['192.168.254.135:9092'],
api_version=(0,10,1)
,value_serializer=serializer,max_request_size=10485760
)
topic="jumat"
with open("sumut.jpg", "rb") as img_file:
    b64_string = base64.b64encode(img_file.read())
encoded_data=b64_string.decode('utf-8')
sending=encoded_data
print("Lenght:",len(sending))
pesan=['img_file.jpg',sending]
producer.send(topic,pesan)
producer.flush()
print(serializer(pesan))
