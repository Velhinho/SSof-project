from CFGraph.Block import Block

class StmtExprBlock(Block):
  def __init__(self, stmt_expr, next_block) -> None:
    self.stmt_expr = stmt_expr
    self.next_block = next_block

  def taint_analysis(self, env):
    self.stmt_expr.eval(env)
    self.next_block.taint_analysis(env)

  def print(self):
    print(self.stmt_expr)
    self.next_block.print()