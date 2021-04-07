import paho.mqtt.client as mqtt
import threading

a = None

def on_connect(client, userdata, flags, rc):
    client.subscribe('topic')

def on_message(client, userdata, msg):
    global a
    if msg.payload.decode() != a:
        print(msg.payload.decode())
    else:
        a = None

client = mqtt.Client()

client.connect('172.17.0.1', 1883, 60)

def mes():
    client.on_connect = on_connect
    client.on_message = on_message

    client.loop_forever()

t1 = threading.Thread(target = mes)
t1.start()

while True:
    b = input()
    a = b
    client.publish('topic', b)

