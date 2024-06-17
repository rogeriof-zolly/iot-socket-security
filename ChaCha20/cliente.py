# echo-client.py
import time
import socket
import json
from faker import Faker
from base64 import b64encode
from Crypto.Cipher import ChaCha20
from mockKMS import MockKMS


start_time = time.perf_counter_ns()
HOST = "127.0.0.1"
PORT = 65432

kms_client = MockKMS()


faker = Faker("pt_BR")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    plate = faker.license_plate().encode()

    obj = ChaCha20.new(key=kms_client.get_encryption_key().encode())
    nonce = obj.nonce
    ct = obj.encrypt(plate)

    data = nonce + ct

    s.sendall(b64encode(data))
    data = s.recv(1024)

print(f"Received {data!r}")
print(f'Encryption time for ChaCha20: {time.perf_counter_ns() - start_time} nanoseconds')