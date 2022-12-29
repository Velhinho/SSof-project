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
    try:
      func_label = env.get_label(self.name)
    except KeyError:
      func_label = Policy.top()
      env.set_label(self.name, func_label)
    args_labels = [arg.eval(env) for arg in self.args]
    # max_label = functools.reduce(lambda l1, l2: Policy.glb(l1, l2), labels)
    arg_label = Policy.top()
    for lab in args_labels:
      arg_label = Policy.glb(arg_label, lab)
    final_label = Policy.glb(func_label, arg_label)
    env.set_label(self.name, final_label)
    return final_label