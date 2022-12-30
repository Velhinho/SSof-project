import Policy
from Ast.Node import Node

class Expr_Assign(Node):
  def __init__(self, var: str, expr_node: Node):
    self.var = var
    self.expr = expr_node

  def __repr__(self) -> str:
    return f"Expr_Assign ({self.var}, {self.expr})"

  def print(self, indentation):
    print("  " * indentation + "Expr_Assign (")
    print("  " * (indentation + 1) + self.var)
    self.expr.print(indentation + 1)
    print("  " * indentation + ")")

  # $a = b()
  # get_label(a) -> {"level": "T", "sources": [a, b]}

  def eval(self, env):
    expr_lab = self.expr.eval(env)
    try:
      var_lab = env.get_label(self.var)
    except KeyError:
      var_lab = Policy.top()
    lab = Policy.glb(expr_lab, var_lab)
    env.set_label(self.var, lab)
    return lab