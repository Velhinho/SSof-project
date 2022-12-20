import sys
import json

def parse(json_ast):
  pass

def main():
  if len(sys.argv == 4):
    with open(sys.argv[1], "r") as slice_f, open(sys.argv[2], "r") as patterns_f, open(sys.argv[3], "r") as out_f:
      json_ast = json.loads(slice_f.read())
      ast = parse()
      ast.eval(env, patterns)