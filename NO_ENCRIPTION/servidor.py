# echo-server.py
import time
import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from mockKMS import MockKMS

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65431  # Port to listen on (non-privileged ports are > 1023)

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
              text = data.decode()
              print(f'Decryption time for No Encription: {time.perf_counter_ns() - start_time} nanoseconds')
              print(text)
              conn.sendall(data)