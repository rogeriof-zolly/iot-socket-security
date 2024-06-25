# echo-client.py
import time
import socket
from faker import Faker

from Crypto.Cipher import AES, PKCS1_OAEP
from sha256 import calculate_hash
from Crypto.Util.Padding import pad
from Crypto.PublicKey import RSA
from mockKMS import MockKMS
import base64

start_time = time.perf_counter_ns()

HOST = "127.0.0.1"
PORT = 65431 

kms_client = MockKMS()

obj = AES.new(kms_client.get_encryption_key().encode(), AES.MODE_CBC, kms_client.get_initialization_vector())

key = RSA.import_key(open('mycert.pem').read())

faker = Faker("pt_BR")
cipher = PKCS1_OAEP.new(key=key)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    plate = faker.license_plate()
    hash_calculation = calculate_hash(plate)

    message = (plate + hash_calculation).encode()

    post_rsa_message = cipher.encrypt(message)
    base64_bytes = base64.b64encode(post_rsa_message)

    text = pad(base64_bytes, 16)
    ciphertext = obj.encrypt(text)

    s.sendall(ciphertext)
    data = s.recv(1024)

print(f"Received {data!r}")
print(f'Encryption time for AES: {time.perf_counter_ns() - start_time} nanoseconds')
