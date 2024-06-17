# echo-server.py
import time
import socket
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from sha256 import calculate_hash
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
              obj = AES.new(kms_client.get_encryption_key().encode(), AES.MODE_CBC, kms_client.get_initialization_vector())

              text = unpad(obj.decrypt(data), 16)
              hash_received = text[-64:].decode()
              message_hash = calculate_hash(text[:-64].decode())
              if hash_received != message_hash:
                print("Hashes are different")
                break
              print(f'Decryption time for AES: {time.perf_counter_ns() - start_time} nanoseconds')
              print(text[:-64])
              conn.sendall(text)