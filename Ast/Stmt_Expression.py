from Ast.Node import Node
from CFGraph.StmtExprBlock import Stmt_Expr_Block

class Stmt_Expression(Node):
  def __init__(self, expr_node: Node):
    self.expr_node = expr_node

  def __repr__(self) -> str:
    return f"Stmt_Expression ({self.expr_node})"

  def build_cfg(self, next_block):
    return Stmt_Expr_Block(self, next_block)

  def print(self, indentation):
    print("  " * indentation + "Stmt_Expression (")
    self.expr_node.print(indentation + 1)
    print("  " * indentation + ")")

  def eval(self, env):
    return self.expr_node.eval(env)