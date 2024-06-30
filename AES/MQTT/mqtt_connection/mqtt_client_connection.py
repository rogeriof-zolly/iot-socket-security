import paho.mqtt.client as mqtt
from mqtt_connection.callbacks import on_connect, on_subscribe, on_message


class MqttClientConnection:
  def __init__(self, broker_ip: str, port: int, client_name: str, keepalive=60) -> None:
    self.__broker_ip = broker_ip
    self.__port = port
    self.__client_name = client_name
    self.__keepalive = keepalive
    self.__mqtt_client = None

  def start_connection(self):
    self.__mqtt_client = mqtt.Client(client_id=self.__client_name)
    self.__mqtt_client.on_connect = on_connect
    self.__mqtt_client.on_subscribe = on_subscribe
    self.__mqtt_client.on_message = on_message
    self.__mqtt_client.connect(self.__broker_ip, self.__port, self.__keepalive)
    self.__mqtt_client.loop_start()

  def end_connection(self):
    try:
      self.__mqtt_client.loop_stop()
      self.__mqtt_client.disconnect()
      return True
    except:
      return False
