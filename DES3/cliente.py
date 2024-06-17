# echo-client.py
import time
import socket
from faker import Faker

from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad
from mockKMS import MockKMS

start_time = time.perf_counter_ns()

HOST = "127.0.0.1"
PORT = 65431 

kms_client = MockKMS()

obj = DES3.new(kms_client.get_encryption_key().encode(), DES3.MODE_OFB, kms_client.get_initialization_vector())

faker = Faker("pt_BR")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    plate = faker.license_plate()

    text = pad(plate.encode(), 16)
    ciphertext = obj.encrypt(text)

    s.sendall(ciphertext)
    data = s.recv(1024)

print(f"Received {data!r}")
print(f'Encryption time for DES3: {time.perf_counter_ns() - start_time} nanoseconds')