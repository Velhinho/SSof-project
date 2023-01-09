from Ast.Node import Node

class Expr_ArrayDimFetch(Node):
  def __init__(self, var, dim) -> None:
    self.var = var
    self.dim = dim

  def __repr__(self) -> str:
    return f"Expr_ArrayDimFetch ({self.var}, {self.dim})"

  def eval(self, env):
    var_lab = self.var.eval(env)
    dim_lab = self.dim.eval(env)
    explicit_lab = var_lab.glb(dim_lab)
    return explicit_lab.glb(env.pc) if env.implicit else explicit_lab