import sys, json, json_parse, connect_stmts, builtins
from Environment import *
from Policy import *
from CFGraph.EndBlock import EndBlock

def eval():
  slices_filename = sys.argv[1]
  patterns_filename = sys.argv[2]
  with open(slices_filename, "r") as slice_f, open(patterns_filename, "r") as patterns_f:
    json_nodes = json.loads(slice_f.read())
    patterns = json.loads(patterns_f.read())
    output = []
    for pattern in patterns:
      env = Environment(pattern)
      ast = json_parse.parse_stmts(json_nodes)
  #    print(ast)
      first_block = connect_stmts.connect_stmts(ast, EndBlock())
      first_block.taint_analysis(env)
      #print(env.illegal_flows)
      pattern_outputs = create_output(pattern, env)
      for pattern_output in pattern_outputs:
        output.append(pattern_output)
    #pretty print
    print(json.dumps(output, indent=4))

def create_output(pattern, env):
  outputs = {}
  for illegal_flow in env.illegal_flows:
    illegal_output = {}
    illegal_output['vulnerability'] = pattern['vulnerability']
    illegal_output['unsanitized flows'] = "no"
    illegal_output['sink'] = illegal_flow['sink']
    sink = illegal_output['sink']
    illegal_output['sanitized flows'] = []
    label = builtins.eval(illegal_flow['label'].__repr__())
    for flow in label['flows']:
      illegal_output['source'] = flow['source']
      source = illegal_output['source']
      if (sink, source) in outputs:
        outputs[(sink, source)]['sanitized flows'].append(flow['sanitizers'])
      else:
        illegal_output['sanitized flows'].append(flow['sanitizers'])
        outputs[(sink, source)] = illegal_output
  for pair, output in outputs.items():
    if [] in output['sanitized flows']:
      output['unsanitized flows'] = "yes"
  return outputs.values()
          

  #    return ast.eval(env, patterns)

eval()