import Policy
from Ast.Node import Node

class Expr_ConstFetch(Node):
  def __init__(self, name) -> None:
    self.name = name

  def __repr__(self) -> str:
    return f"Scalar ({self.name})"

  def print(self, indentation):
    print("  " * indentation + str(self))

  def eval(self, env):
    return Policy.top()