import sys
import json
import json_parse
from Environment import *
from Policy import *

def eval():
  slices_filename = sys.argv[1]
  patterns_filename = sys.argv[2]
  with open(slices_filename, "r") as slice_f, open(patterns_filename, "r") as patterns_f:
    json_nodes = json.loads(slice_f.read())
    patterns = json.loads(patterns_f.read())
    labenv = Environment(patterns[0])
    ast = json_parse.parse(json_nodes)
    for node in ast:
      node.print(0)
      print()
#    return ast.eval(env, patterns)

def test():
  output_filename = sys.argv[3] 
  with open(output_filename, "r") as output_f:
    expected_output = output_f.read()
    actual_output = json.dumps(eval())
    if expected_output != actual_output:
      print(f"Failed for {output_filename}")
    else:
      print("Success")
    print(f"Result: \n{actual_output}")

eval()