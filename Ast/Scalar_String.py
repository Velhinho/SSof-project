from Ast.Node import Node

class Scalar_String(Node):
  def __init__(self, value: str):
    self.value = value

  def __repr__(self) -> str:
    return f"Scalar_String ({self.value})"

  def print(self, indentation):
    print("  " * indentation + str(self))