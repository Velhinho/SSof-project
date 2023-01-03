class Flow:
  def __init__(self, source, sanitizers) -> None:
    self.source = source
    self.sanitizers = sanitizers
  
  def __repr__(self) -> str:
    return str(self.__dict__)

  def add_sanitizer(self, sanitizer):
    return Flow(self.source, self.sanitizers + [sanitizer])
  
class Label:
  def __init__(self, level, flows) -> None:
    self.level = level
    self.flows = flows

  def __repr__(self) -> str:
    return str(self.__dict__)

  def add_sanitizer(self, sanitizer):
    flows = [flow.add_sanitizer(sanitizer) for flow in self.flows]
    return Label(self.level, flows)

  def is_bottom(self):
    return self.level == "T"
  
  def glb(self, lab):
    if self.is_bottom() and lab.is_bottom():
      flows = self.flows + lab.flows
      return Label("T", flows)
    elif self.is_bottom():
      return self
    else:
      return lab

def bottom(src):
  return Label("T", [Flow(source=src, sanitizers=[])])

def top():
  return Label("UT", [Flow(source=None, sanitizers=[])])