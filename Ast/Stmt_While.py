from Ast.Node import Node
from connect_stmts import connect_stmts
from CFGraph.LoopStartBlock import LoopStartBlock
from CFGraph.LoopEndBlock import LoopEndBlock

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
    loop_end = LoopEndBlock(next_block)
    while_block = connect_stmts(self.stmts, loop_end)
    loop_start = LoopStartBlock(loop_end)
    loop_end.loop_start_block = loop_start
    loop_end.cond_expr = self.cond_expr
    loop_end.while_block = while_block
    return loop_start