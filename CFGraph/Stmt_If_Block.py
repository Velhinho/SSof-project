from CFGraph.Block import Block

class Stmt_If_Block(Block):
  def __init__(self, cond_expr, if_block, else_block) -> None:
    self.cond_expr = cond_expr
    self.if_block = if_block
    self.else_block = else_block
  
  def taint_analysis(self, env):
    self.cond_expr.eval(env) # necessary for implicit flows
    old_labels = env.get_labels_copy()
    self.if_block.taint_analysis(env)
    env.set_labels(old_labels)
    self.else_block.taint_analysis(env)

  def print(self):
    print("BRANCH")
    print(self.cond_expr)
    self.if_block.print()
    self.else_block.print()