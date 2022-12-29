class Stmt_Expr_Block:
  def __init__(self, stmt_expr, next_block) -> None:
    self.stmt_expr = stmt_expr
    self.next_block = next_block

  def propagate(self, env, policy):
    self.stmt_expr.eval(env, policy)
    self.next_block.propagate(env, policy)

  def print(self):
    print(self.stmt_expr)
    self.next_block.print()