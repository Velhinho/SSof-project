from Ast.Expr_Assign import Expr_Assign
from Ast.Expr_FuncCall import Expr_FuncCall
from Ast.Expr_Variable import Expr_Variable
from Ast.Scalar import Scalar
from Ast.Stmt_Expression import Stmt_Expression
from Ast.Stmt_If import Stmt_If
from Ast.BoolExpr import BoolExpr

def parse_scalar(json_node):
  value = json_node["value"]
  return Scalar(value=value)

def parse_expr_variable(json_node):
  name = json_node["name"]
  return Expr_Variable(name=name)

def parse_expr_assign(json_node):
  var = json_node["var"]["name"]
  expr_node = parse_expression(json_node["expr"])
  return Expr_Assign(var=var, expr_node=expr_node)

def parse_expr_func_call(json_node):
  name = json_node["name"]["parts"][0]
  args = []
  for arg in json_node["args"]:
    node = parse_expression(arg["value"])
    args.append(node)
  return Expr_FuncCall(name=name, args=args)

def parse_bool_expr(json_node):
  left = parse_expression(json_node["left"])
  right = parse_expression(json_node["right"])
  return BoolExpr(left_node=left, right_node=right)

def parse_expression(json_node):
  scalars = ["Scalar_String", "Scalar_LNumber"]
  bool_expr = ["Expr_BinaryOp_Greater", "Expr_BinaryOp_Smaller"]
  nodeType = json_node["nodeType"]
  if nodeType in scalars:
    return parse_scalar(json_node)
  elif nodeType == "Expr_Variable":
    return parse_expr_variable(json_node)
  elif nodeType == "Expr_Assign":
    return parse_expr_assign(json_node)
  elif nodeType == "Expr_FuncCall":
    return parse_expr_func_call(json_node)
  elif nodeType in bool_expr:
    return parse_bool_expr(json_node)
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

def parse_stmt(json_node):
  nodeType = json_node["nodeType"]
  if nodeType == "Stmt_Expression":
    return parse_stmt_expression(json_node)
  elif nodeType == "Stmt_If":
    return parse_stmt_if(json_node)
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