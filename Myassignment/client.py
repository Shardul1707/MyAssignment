import paho.mqtt.client as mqtt
import random
import time

broker = "localhost"
port = 1883
topic = "upswing/data"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker...")
    else:
        raise Exception(f"Connection failed with code {rc}")

client = mqtt.Client()

client.on_connect = on_connect

client.connect(broker, port)
client.loop_start()

try:
    while True:
        message = {
            "status": random.randint(0, 6)
        }
        client.publish(topic, str(message))
        print(f"Published: {message}")
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping the publisher...")
    client.loop_stop()
    client.disconnect()