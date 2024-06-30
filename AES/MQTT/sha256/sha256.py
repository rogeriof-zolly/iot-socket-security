import hashlib


# The function encrypt should encrypt a message using the sha256 algorithm
def calculate_hash(message):
  return hashlib.sha256(message.encode()).hexdigest()
