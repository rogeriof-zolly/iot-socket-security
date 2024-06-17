# echo-server.py
import time
import socket
import json
from Crypto.Cipher import ChaCha20
from mockKMS import MockKMS
from base64 import b64decode


HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

kms_client = MockKMS()

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
              
              data = b64decode(data)

              nonce = data[:8]
              data = data[8:]

              obj = ChaCha20.new(key=kms_client.get_encryption_key().encode(), nonce=nonce)

              text = obj.decrypt(data)
              print(f'Decryption time for ChaCha20: {time.perf_counter_ns() - start_time} nanoseconds')
              conn.sendall(text)