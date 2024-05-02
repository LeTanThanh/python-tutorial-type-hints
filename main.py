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
