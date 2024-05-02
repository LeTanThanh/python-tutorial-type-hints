if __name__ == "__main__":
  # Introduction to Python type hints

  def say_hi(name: str) -> str:
    return f"Hi {name}"

  print(say_hi("John"))

  """
  It's important to note that the Python interpreter ignores type hints completely.
  If you pass a number to the say_hi() function, the program will run without any warning or error:
  """

  print(say_hi(123))

  """
  To check the syntax for type hints, you neef use a static type checker tool.
  """

  # Using a static type checker tool: mypy

  """
  pip install mypy

  mypy main.py
  """

  # Type hinting & type inference

  name: str = "John"
  name = 100
  # Error: Incompatible types in assignment

  name = "John"
  name = 100
  # Error: Incompatible types in assignment

  # Adding type hints for multiple types

  # def add(x, y):
  #   return x + y

  # print(add(1, 2))

  # from typing import Union

  # def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
  #   return x + y

  # print(add(1, 2))

  def add(x: int | float, y: int | float) -> int | float:
    return x + y

  print(add(1, 2))

  # Type aliases

  from typing import Union

  number = Union[int, float]

  def add(x: number, y: number) -> number:
    return x + y

  print(add(1, 2))

  # Adding type hints for lists, dictionaries, and sets

  """
  You can use the following built-in types to set the types hiones for a list, dictionary, and set:
  - list
  - dict
  - set

  If you type hones in a variable as a list but later assign a dictionary to it, you'll get an error
  """

  ratings: list = [1, 2, 3]
  ratings = {1: "Bad", 2: "average", 3: "Good"}

  # error: Incompatible types in assignment

  """
  To specify the types of values in a list, dictionary, and sets, you can use types aliases from the typing module:

  - List: list
  - Tuple: tuple
  - Dict: dict
  - Set: set
  - Frozenset: frozenset
  - Sequence: For list, tuple, and any pther sequence data type.
  - Mapping: For dictionary (dict), set, frozenset, and any other mapping data type
  - ByteString: bytes, bytearray, and mempryview types.

  For example, the following defines a list of integers:
  """

  from typing import List

  ratings: List[int] = [1, 2, 3]
