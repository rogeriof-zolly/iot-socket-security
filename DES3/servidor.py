# echo-server.py
import time
import socket
from Crypto.Cipher import DES3
from Crypto.Util.Padding import unpad
from mockKMS import MockKMS

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65431  # Port to listen on (non-privileged ports are > 1023)

kms_client = MockKMS()

obj = DES3.new(kms_client.get_encryption_key().encode(), DES3.MODE_OFB, kms_client.get_initialization_vector())


while True:
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.bind((HOST, PORT))
      s.listen()
      conn, addr = s.accept()
      with conn:
          print(f"Connected by {addr}")
          while True:
              data = conn.recv(1024)
              if not data:
                  break
              
              start_time = time.perf_counter_ns()

              text = unpad(obj.decrypt(data), 16)
              print(f'Decryption time for DES3: {time.perf_counter_ns() - start_time} nanoseconds')
              print(text)
              conn.sendall(text)