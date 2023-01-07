from Ast.Node import Node
from CFGraph.StmtIfBlock import Stmt_If_Block
from connect_stmts import connect_stmts

class Stmt_If(Node):
  def __init__(self, cond_expr, if_stmts, else_stmts) -> None:
    self.cond_expr = cond_expr
    self.if_stmts = if_stmts
    self.else_stmts = else_stmts if else_stmts is not None else []

  def __repr__(self) -> str:
    return f"Stmt_If ({self.cond_expr, self.if_stmts, self.else_stmts})"
    
  def build_cfg(self, next_block):
    if_block = connect_stmts(self.if_stmts, next_block)
    else_block = connect_stmts(self.else_stmts, next_block)
    return Stmt_If_Block(self.cond_expr, if_block, else_block)

  def print(self, indentation):
    print("  " * indentation + "Stmt_If (")
    print("  " * indentation + "cond_expr")
    self.cond_expr.print(indentation + 1)
    
    print("  " * (indentation + 1) + "if_stmts")
    for stmt in self.if_stmts:
      stmt.print(indentation + 1)

    print("  " * (indentation + 1) + "else_stmts")
    for stmt in self.else_stmts:
      stmt.print(indentation + 1)

    print("  " * indentation + ")")
