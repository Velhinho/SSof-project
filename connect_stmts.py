def connect_stmts(stmts, end_block):
  next_block = end_block
  block = end_block
  for stmt in reversed(stmts):
    block = stmt.build_cfg(next_block)
    next_block = block
  return block

# stmt = [A, B], endblock = Endblock()
# B -> Endblock
# A -> B
# A -> B -> Endblock