import Policy

class Environment:
  def __init__(self, pattern):
    self.labels = {}
    self.sources = pattern["sources"].copy()
    self.sinks = pattern["sinks"].copy()
    self.sanitizers = pattern["sanitizers"].copy()
    for source in self.sources:
      self.labels[source] = Policy.bottom(source)
    for sink in self.sinks:
      self.labels[sink] = Policy.top()
    for sanitizer in self.sanitizers:
      self.labels[sanitizer] = Policy.top()
    self.implicit = pattern["implicit"] == "yes"
    # stores context
    self.pc = Policy.top()
    self.illegal_flows = []

  def __repr__(self) -> str:
    return str(self.__dict__)

  def set_pc(self, label):
    self.pc = label

  def get_labels_copy(self):
    return self.labels.copy()

  def set_labels(self, labels):
    self.labels = labels

  def get_label(self, variable):
    return self.labels[variable]
  
  def add_illegal_flow(self, sink, label):
    self.illegal_flows.append({"sink": sink, "label": label})

  def set_label(self, variable, lab):
    self.labels[variable] = lab

  def allow_implicit(self):
    return self.implicit