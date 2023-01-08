from CFGraph.Block import Block

class LoopEndBlock(Block):
  def __init__(self, next_block) -> None:
    self.loop_start_block = None
    self.cond_expr = None
    self.while_block = None
    self.next_block = next_block
    self.loop_counter = 0


  def run_body(self, env):
      cond_lab = self.cond_expr.eval(env)
      env.set_pc(cond_lab.glb(env.pc))
      self.while_block.taint_analysis(env)

  def taint_analysis(self, env):
    if self.loop_counter == 0:
      old_labels = env.get_labels_copy()
      old_pc = env.pc

      # RUN BODY TWICE
      self.loop_counter = 1
      self.run_body(env)
      env.set_labels(old_labels) # reset labels before next path

      # RUN BODY ONCE
      self.loop_counter = 2
      self.run_body(env)
      env.set_labels(old_labels) # reset labels before next path

      # SKIP BODY
      env.set_pc(old_pc)
      self.loop_counter = 0
      self.cond_expr.eval(env)
      self.next_block.taint_analysis(env)
    elif self.loop_counter == 1:
      self.loop_counter = 2
      self.run_body(env)
    elif self.loop_counter == 2:
      self.cond_expr.eval(env)
      self.next_block.taint_analysis(env)

  def print(self):
    if self.loop_counter == 0:
      print("RUN BODY TWICE PATH")
      self.loop_counter = 1
      print(self.cond_expr)
      self.while_block.print()

      print("RUN BODY ONCE")
      self.loop_counter = 2
      print(self.cond_expr)
      self.while_block.print()

      print("SKIP BODY")
      self.loop_counter = 0
      print(self.cond_expr)
      self.next_block.print()
    elif self.loop_counter == 1:
      self.loop_counter = 2
      print(self.cond_expr)
      self.while_block.print()
    elif self.loop_counter == 2:
      print(self.cond_expr)
      self.next_block.print()
