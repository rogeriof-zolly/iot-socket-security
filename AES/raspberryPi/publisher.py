import paho.mqtt.client as mqtt
import time
import socket
from faker import Faker
from Crypto.Cipher import AES, PKCS1_OAEP
from sha256 import calculate_hash
from Crypto.Util.Padding import pad
from Crypto.PublicKey import RSA
from mockKMS import MockKMS
import base64

mqtt_client = mqtt.Client(callback_api_version=2, client_id='AES Publisher')
mqtt_client.connect(host='localhost', port=1883)

kms_client = MockKMS()

obj = AES.new(kms_client.get_encryption_key().encode(),
              AES.MODE_CBC, kms_client.get_initialization_vector())

key = RSA.import_key(open('mycert.pem').read())

faker = Faker("pt_BR")
cipher = PKCS1_OAEP.new(key=key)

plate = faker.license_plate()
hash_calculation = calculate_hash(plate)

message = (plate + hash_calculation).encode()

post_rsa_message = cipher.encrypt(message)
base64_bytes = base64.b64encode(post_rsa_message)

text = pad(base64_bytes, 16)
ciphertext = obj.encrypt(text)


mqtt_client.publish('/messages', ciphertext)
