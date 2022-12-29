from Ast.Node import Node

class BoolExpr(Node):
  def __init__(self, left_node, right_node) -> None:
    self.left_node = left_node
    self.right_node = right_node

  def __repr__(self) -> str:
    return f"BoolExpr ({self.left_node, self.right_node})"

  def print(self, indentation):
    print("  " * indentation + str(self))

  def eval(self, env, policy):
    pass