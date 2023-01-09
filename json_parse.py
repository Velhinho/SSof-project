from Ast.Expr_Assign import Expr_Assign
from Ast.Expr_FuncCall import Expr_FuncCall
from Ast.Expr_Variable import Expr_Variable
from Ast.Scalar import Scalar
from Ast.Stmt_Expression import Stmt_Expression
from Ast.Stmt_If import Stmt_If
from Ast.Stmt_While import Stmt_While
from Ast.BinExpr import BinExpr
from Ast.Expr_ArrayDimFetch import Expr_ArrayDimFetch
from Ast.Expr_ConstFetch import Expr_ConstFetch

def parse_scalar(json_node):
  value = json_node["value"]
  return Scalar(value=value)

def parse_expr_variable(json_node):
  name = json_node["name"]
  return Expr_Variable(name="$" + name)

def parse_const_fetch(json_node):
  name = json_node["name"]["parts"][0]
  return Expr_ConstFetch(name=name)

def parse_expr_assign(json_node):
  var = "$" + json_node["var"]["name"]
  expr_node = parse_expression(json_node["expr"])
  return Expr_Assign(var=var, expr_node=expr_node)

def parse_expr_func_call(json_node):
  name = json_node["name"]["parts"][0]
  args = []
  for arg in json_node["args"]:
    node = parse_expression(arg["value"])
    args.append(node)
  return Expr_FuncCall(name=name, args=args)

def parse_bin_expr(json_node):
  left = parse_expression(json_node["left"])
  right = parse_expression(json_node["right"])
  return BinExpr(left_node=left, right_node=right)

def parse_arraydimfetch(json_node):
  var = parse_expr_variable(json_node["var"])
  dim = parse_scalar(json_node["dim"])
  return Expr_ArrayDimFetch(var=var, dim=dim)

def parse_expression(json_node):
  nodeType = json_node["nodeType"]
  if nodeType[:6] == "Scalar":
    return parse_scalar(json_node)
  elif nodeType == "Expr_ConstFetch":
    return parse_const_fetch(json_node)
  elif nodeType == "Expr_Variable":
    return parse_expr_variable(json_node)
  elif nodeType in ["Expr_Assign", "Expr_AssignOp_Plus"]:
    return parse_expr_assign(json_node)
  elif nodeType == "Expr_FuncCall":
    return parse_expr_func_call(json_node)
  elif nodeType[:13] == "Expr_BinaryOp":
    return parse_bin_expr(json_node)
  elif nodeType == "Expr_ArrayDimFetch":
    return parse_arraydimfetch(json_node)
  elif nodeType in ["Expr_PreInc", "Expr_PreDec", "Expr_PostInc", "Expr_PostDec"]:
    return parse_expr_variable(json_node["var"])
  elif nodeType in ["Expr_BitwiseNot", "Expr_BooleanNot"]:
    return parse_expression(json_node["expr"])
  else:
    raise ValueError("expected expression node")

def parse_stmt_expression(json_node):
  expr_node = parse_expression(json_node["expr"])
  return Stmt_Expression(expr_node=expr_node)

def parse_stmt_if(json_node):
  cond = parse_expression(json_node["cond"])
  if_stmts = parse_stmts(json_node["stmts"])
  else_stmts = parse_stmts(json_node["else"]["stmts"]) if json_node["else"] is not None else None
  return Stmt_If(cond_expr=cond, if_stmts=if_stmts, else_stmts=else_stmts)

def parse_stmt_while(json_node):
  cond = parse_expression(json_node["cond"])
  stmts = parse_stmts(json_node["stmts"])
  return Stmt_While(cond=cond, stmts=stmts)

def parse_stmt_echo(json_node):
  name = "echo"
  exprs = []
  for expr in json_node["exprs"]:
    node = parse_expression(expr)
    exprs.append(node)
  funcCall = Expr_FuncCall(name=name, args=exprs) # echo is basically a call to a function named "echo"
  return Stmt_Expression(funcCall)

def parse_stmt(json_node):
  nodeType = json_node["nodeType"]
  if nodeType == "Stmt_Expression":
    return parse_stmt_expression(json_node)
  elif nodeType == "Stmt_If":
    return parse_stmt_if(json_node)
  elif nodeType == "Stmt_While":
    return parse_stmt_while(json_node)
  elif nodeType == "Stmt_Echo":
    return parse_stmt_echo(json_node)
  elif nodeType in ["Stmt_Break", "Stmt_Continue"]: # Not creating new paths created by breaks or continues
    return None
  elif nodeType == "Stmt_Nop": # Stmt_Nop represents a comment
    return None
  else:
    raise ValueError("expected statement node")

def parse_stmts(json_nodes):
  ast = []
  for node in json_nodes:
    stmt = parse_stmt(node)
    if stmt is not None:
      ast.append(stmt)
  return ast