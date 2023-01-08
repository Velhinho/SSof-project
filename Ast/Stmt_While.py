from Ast.Node import Node
from connect_stmts import connect_stmts
from CFGraph.StmtWhileBlock import StmtWhileBlock

class Stmt_While(Node):
  def __init__(self, cond, stmts) -> None:
    self.cond_expr = cond
    self.stmts = stmts
  
  def __repr__(self) -> str:
    return f"Stmt_while(cond {self.cond_expr} stmts {self.stmts})" 
  
  def print(self, indentation):
    self.cond.print(indentation + 1)
    for stmt in self.stmts:
      stmt.print(indentation + 1)

  def build_cfg(self, next_block):
    while_block = connect_stmts(self.stmts, next_block)
    return StmtWhileBlock(self.cond_expr, while_block, next_block)