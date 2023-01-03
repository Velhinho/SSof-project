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
    if self.name in env.sanitizers and arg_label.is_bottom():
      arg_label = arg_label.add_sanitizer(self.name)
    if self.name in env.sinks and arg_label.is_bottom():
      env.add_illegal_flow(self.name, arg_label)
    return func_label.glb(arg_label)

def eval_args(args, env):
  args_labels = [arg.eval(env) for arg in args]
  arg_label = Policy.top()
  for lab in args_labels:
    arg_label = arg_label.glb(lab)
  return arg_label