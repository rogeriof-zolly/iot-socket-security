class MockKMS():
  def __init__(self) -> None:
    self.__encryption_key = "ZBmy^!c{$8EK&Emc0tpsV%QpuS(mr?7h"

  def get_encryption_key(self):
    return self.__encryption_key
