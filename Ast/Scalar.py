import Policy
from Ast.Node import Node

class Scalar(Node):
  def __init__(self, value: str):
    self.value = value

  def __repr__(self) -> str:
    return f"Scalar ({self.value})"

  def print(self, indentation):
    print("  " * indentation + str(self))

  def eval(self, env):
    return Policy.top()