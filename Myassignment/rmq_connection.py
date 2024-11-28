import paho.mqtt.client as mqtt

class Rmq_connect:
    def __init__(self):
        self.broker = "localhost"
        self.port = 1883
        self.topic = "upswing/data"

    def connect(self):
        client = mqtt.Client()
        return client