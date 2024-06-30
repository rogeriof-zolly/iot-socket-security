import time
from config.broker_configs import mqtt_broker_configs
from mqtt_connection.mqtt_client_connection import MqttClientConnection


def start():
  mqtt_client_connection = MqttClientConnection(
      mqtt_broker_configs["host"],
      mqtt_broker_configs["port"],
      mqtt_broker_configs["client_name"],
      mqtt_broker_configs["keepalive"]
  )

  mqtt_client_connection.start_connection()

  while True:
    time.sleep(0.001)
