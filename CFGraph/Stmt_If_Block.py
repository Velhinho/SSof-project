class Stmt_If_Block:
  def __init__(self, cond_expr, if_block, else_block) -> None:
    self.cond_expr = cond_expr
    self.if_block = if_block
    self.else_block = else_block
  
  def propagate(self, env, policy):
    self.cond_expr.eval(env, policy)
    self.if_block.propagate(env, policy)
    self.else_block.propagate(env, policy)

  def print(self):
    print("BRANCH")
    print(self.cond_expr)
    self.if_block.print()
    self.else_block.print()