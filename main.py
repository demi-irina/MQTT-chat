import paho.mqtt.client as mqtt
import threading
import json
import random

c = None

def on_connect(client, userdata, flags, rc):
    client.subscribe('topic')

def on_message(client, userdata, msg):
    global c
    if msg.payload.decode() != c:
        print(json.loads(msg.payload.decode()))
    else:
        c = None

def loop():
    client.loop_forever()

client = mqtt.Client()
client.connect('172.17.0.1', 1883, 60)
client.on_connect = on_connect
client.on_message = on_message

name = input('Enter your name: ')
a = '\033[' + str(random.randint(31, 36)) + 'm'
color = a + name + ': ' + '\033[0m'

t1 = threading.Thread(target = loop)
t1.start()

while True:
    b = input()
    c = json.dumps(color + b)
    client.publish('topic', c)

