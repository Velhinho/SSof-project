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

  def eval(self, env):
    expr_lab = self.expr.eval(env)
    try:
      var_lab = env.get_label(self.var)
    except KeyError:
      var_lab = Policy.top()
    lab = Policy.glb(expr_lab, var_lab)
    if self.var in env.sinks and Policy.is_bottom(lab):
      env.add_illegal_flow(self.var, Policy.get_sources(lab), Policy.get_sanitizers(lab))
    env.set_label(self.var, lab)
    return lab