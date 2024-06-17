# echo-client.py
import time
import socket
from faker import Faker

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad
from mockKMS import MockKMS

start_time = time.perf_counter_ns()
HOST = "127.0.0.1"
PORT = 65431

kms_client = MockKMS()


faker = Faker("pt_BR")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    plate = faker.license_plate()
    
    obj = DES.new(kms_client.get_encryption_key().encode(), DES.MODE_OFB)

    ciphertext = obj.encrypt(plate.encode())
    data = obj.iv + ciphertext

    s.sendall(data)
    data = s.recv(1024)

print(f"Received {data!r}")
print(f'Encryption time for DES: {time.perf_counter_ns() - start_time} nanoseconds')