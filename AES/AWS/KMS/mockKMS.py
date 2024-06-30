class MockKMS():
  def __init__(self) -> None:
    self.__encryption_key = "<)HMz9fr8jZ>6jQ$"
    self.__initialization_vector = b'This is an IV456'

  def get_encryption_key(self):
    return self.__encryption_key
  
  def get_initialization_vector(self):
    return self.__initialization_vector