from Ast.Node import Node

class Stmt_Expression(Node):
  def __init__(self, expr_node: Node):
    self.expr_node = expr_node

  def __repr__(self) -> str:
    return f"Stmt_Expression ({self.expr_node})"

  def print(self, indentation):
    print("  " * indentation + "Stmt_Expression (")
    self.expr_node.print(indentation + 1)
    print("  " * indentation + ")")
