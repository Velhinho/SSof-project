from Ast.Node import Node

class Expr_Variable(Node):
  def __init__(self, name: str):
    self.name = name

  def __repr__(self) -> str:
    return f"Expr_Variable ({self.name})"

  def print(self, indentation):
    print("  " * indentation + str(self))