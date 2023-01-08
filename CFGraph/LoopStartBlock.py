class LoopStartBlock:
  def __init__(self, loop_end_block) -> None:
    self.loop_end_block = loop_end_block

  def taint_analysis(self, env):
    self.loop_end_block.taint_analysis(env)

  def print(self):
    print("LOOP START")
    self.loop_end_block.print()