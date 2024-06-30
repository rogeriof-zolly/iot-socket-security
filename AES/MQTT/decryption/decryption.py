from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import unpad
from sha256.sha256 import calculate_hash
from KMS.mockKMS import MockKMS
import base64


def decryptMessage(message):
  kms_client = MockKMS()

  obj = AES.new(kms_client.get_encryption_key().encode(),
                AES.MODE_CBC, kms_client.get_initialization_vector())
  key = RSA.import_key(open('mycert.key').read())
  cipher = PKCS1_OAEP.new(key)

  aes_decrypted = unpad(obj.decrypt(message), 16)
  base64_bytes = base64.b64decode(aes_decrypted)
  text = cipher.decrypt(base64_bytes)

  hash_received = text[-64:].decode()
  message_hash = calculate_hash(text[:-64].decode())

  if hash_received != message_hash:
    print("Hashes are different")
    return False

  print("Message decrypted:", text[:-64])
  return True
