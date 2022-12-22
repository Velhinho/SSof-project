from Ast.Node import Node

class Expr_FuncCall(Node):
  def __init__(self, name: str, args: list):
    self.name = name
    self.args = args

  def __repr__(self) -> str:
    return f"Expr_FuncCall ({self.name}, {self.args})"

  def print(self, indentation):
    print("  " * indentation + "Expr_FuncCall (")
    print("  " * (indentation + 1) + self.name)
    for arg in self.args:
      arg.print(indentation + 1)
    print("  " * indentation + ")")