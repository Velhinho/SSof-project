class Node:
  pass

class Scalar_String(Node):
  def __init__(self, value: str):
    self.value = value

  def __repr__(self) -> str:
    return f"Scalar_String ({self.value})"

  def print(self, indentation):
    print("  " * indentation + str(self))

class Expr_Variable(Node):
  def __init__(self, name: str):
    self.name = name

  def __repr__(self) -> str:
    return f"Expr_Variable ({self.name})"

  def print(self, indentation):
    print("  " * indentation + str(self))

class Expr_Assign(Node):
  def __init__(self, var: str, expr_node: Node):
    self.var = var
    self.expr = expr_node

  def __repr__(self) -> str:
    return f"Expr_Assign ({self.var}, {self.expr})"

  def print(self, indentation):
    print("  " * indentation + "Expr_Assign (")
    print("  " * (indentation + 1) + self.var)
    self.expr.print(indentation + 1)
    print("  " * indentation + ")")

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

class Stmt_Expression(Node):
  def __init__(self, expr_node: Node):
    self.expr_node = expr_node

  def __repr__(self) -> str:
    return f"Stmt_Expression ({self.expr_node})"

  def print(self, indentation):
    print("  " * indentation + "Stmt_Expression (")
    self.expr_node.print(indentation + 1)
    print("  " * indentation + ")")
