import Policy
from Ast.Node import Node
import functools

class Expr_FuncCall(Node):
  def __init__(self, name: str, args: list):
    self.name = name
    self.args = args

  def __repr__(self) -> str:
    return f"Expr_FuncCall ({self.name}, {self.args})"

  def print(self, indentation):
    print("  " * indentation + "Expr_FuncCall (")
    print("  " * (indentation + 1) + self.name)
    for arg in self.args:
      arg.print(indentation + 1)
    print("  " * indentation + ")")

  def reduce(f, l):
    ret = l[0]
    for elem in l:
      ret = f(ret, elem)
    return ret

  def eval(self, env):
    func_label = Policy.bottom(self.name) if self.name in env.sources else Policy.top()
    arg_label = eval_args(self.args, env)
    if self.name in env.sanitizers and Policy.is_bottom(arg_label):
      Policy.add_sanitizer(arg_label, self.name)
    if self.name in env.sinks and Policy.is_bottom(arg_label):
      env.add_illegal_flow(self.name, Policy.get_sources(arg_label), Policy.get_sanitizers(arg_label))
    return Policy.glb(func_label, arg_label)

def eval_args(args, env):
  args_labels = [arg.eval(env) for arg in args]
  arg_label = Policy.top()
  for lab in args_labels:
    arg_label = Policy.glb(arg_label, lab)
  return arg_label