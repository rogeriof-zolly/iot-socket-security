from config.broker_configs import mqtt_broker_configs
import base64
from decryption.decryption import decryptMessage

# def decryptMessage(message):
#   kms_client = MockKMS()

#   obj = AES.new(kms_client.get_encryption_key().encode(),
#                 AES.MODE_CBC, kms_client.get_initialization_vector())
#   key = RSA.import_key(open('mycert.key').read())
#   cipher = PKCS1_OAEP.new(key)

#   aes_decrypted = unpad(obj.decrypt(message), 16)
#   base64_bytes = base64.b64decode(aes_decrypted)
#   text = cipher.decrypt(base64_bytes)

#   hash_received = text[-64:].decode()
#   message_hash = calculate_hash(text[:-64].decode())

#   if hash_received != message_hash:
#     print("Hashes are different")
#     return False

#   print(text[:-64])
#   return True


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
