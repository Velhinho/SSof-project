import sys, json, json_parse, connect_stmts
from Environment import *
from Policy import *
from CFGraph.EndBlock import EndBlock

def eval():
  slices_filename = sys.argv[1]
  patterns_filename = sys.argv[2]
  with open(slices_filename, "r") as slice_f, open(patterns_filename, "r") as patterns_f:
    json_nodes = json.loads(slice_f.read())
    patterns = json.loads(patterns_f.read())
    labenv = Environment(patterns[0])
    policy = TUTPolicy()
    ast = json_parse.parse_stmts(json_nodes)
    first_block = connect_stmts.connect_stmts(ast, EndBlock())
    first_block.print()
#    return ast.eval(env, patterns)

eval()