from CFGraph.Block import Block

class EndBlock(Block):
  def print(self):
    print("END")

  def taint_analysis(self, env):
    pass