from Ast import *

def parse_scalar_string(json_node):
  value = json_node["value"]
  return Scalar_String(value=value)

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

def parse_expression(json_node):
  nodeType = json_node["nodeType"]
  if nodeType == "Scalar_String":
    return parse_scalar_string(json_node)
  elif nodeType == "Expr_Variable":
    return parse_expr_variable(json_node)
  elif nodeType == "Expr_Assign":
    return parse_expr_assign(json_node)
  elif nodeType == "Expr_FuncCall":
    return parse_expr_func_call(json_node)
  else:
    raise ValueError("expected expression node")

def parse_stmt_expression(json_node):
  expr_node = parse_expression(json_node["expr"])
  return Stmt_Expression(expr_node=expr_node)

def parse(json_nodes):
  ast = []
  for node in json_nodes:
    nodeType = node["nodeType"]
    if nodeType == "Stmt_Expression":
      expr_node = parse_expression(node["expr"])
      stmt_expr_node = Stmt_Expression(expr_node=expr_node)
      ast.append(stmt_expr_node)
    elif nodeType == "Stmt_Nop": # Stmt_Nop represents a comment
      continue
    else:
      raise ValueError("expected statement node")
  return ast