class Stmt_While_Block:
  def __init__(self, cond, while_block, next_block) -> None:
    self.cond_expr = cond
    self.while_block = while_block
    self.next_block = next_block

  def taint_analysis(self, env):
    self.cond_expr.eval(env) # necessary for implicit flows
    old_labels = env.get_labels_copy()
    self.while_block.taint_analysis(env)
    env.set_labels(old_labels)
    self.next_block.taint_analysis(env)

  def print(self):
    print("LOOP")
    print(self.cond_expr)
    self.while_block.print()
    self.next_block.print()