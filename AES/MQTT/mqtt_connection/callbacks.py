from config.broker_configs import mqtt_broker_configs
from decryption.decryption import decryptMessage


def on_connect(client, userdata, flags, rc):
  if rc == 0:
    print("Connected to broker")
    client.subscribe(mqtt_broker_configs["topic"])
  else:
    print("Connection failed")


def on_subscribe(client, userdata, mid, granted_qos):
  print("Subscribed to topic")
  print("QOS: ", granted_qos)


def on_message(client, userdata, message):
  print("Message received: ", str(message.payload))
  decryptMessage(message.payload)
