from mongo_connection import Mongo_connection
from rmq_connection import Rmq_connect
from datetime import datetime

mongo_connection = Mongo_connection()
rmq_connection = Rmq_connect()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker...")
        client.subscribe(rmq_connection.topic)
    else:
        raise Exception(f"Connection failed with code {rc}")


def on_message(client, userdata, msg):
    print(f"Received Message - {msg.payload.decode()} from topic - {msg.topic}")
    mongo_connection.collection.insert_one({"topic": msg.topic, "message": msg.payload.decode(), "time": datetime.now()})

client = rmq_connection.connect()

client.on_connect = on_connect
client.on_message = on_message

client.connect(rmq_connection.broker, rmq_connection.port)
client.loop_forever()
