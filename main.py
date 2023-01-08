import sys, json, json_parse, connect_stmts, builtins
from Environment import *
from Policy import *
from CFGraph.EndBlock import EndBlock

def eval():
  slices_filename = sys.argv[1]
  patterns_filename = sys.argv[2]
  output_filename = 'output/' + slices_filename.split('/')[1].split('.')[0] + '.output.json'
  with open(slices_filename, "r") as slice_f, open(patterns_filename, "r") as patterns_f, open(output_filename, "w") as output_f:
    json_nodes = json.loads(slice_f.read())
    patterns = json.loads(patterns_f.read())
    output = []
    for pattern in patterns:
      for sink in pattern['sinks']:
        sink_pattern = {
          'vulnerability' : pattern['vulnerability'],
          'sources' : pattern['sources'],
          'sanitizers' : pattern['sanitizers'],
          'sinks' : [sink],
          'implicit' : pattern['implicit']
        }
        env = Environment(sink_pattern)
        ast = json_parse.parse_stmts(json_nodes)
    #    print(ast)
        first_block = connect_stmts.connect_stmts(ast, EndBlock())
        first_block.taint_analysis(env)
        #print(env.illegal_flows)
        pattern_outputs = create_output(sink_pattern, env)
        output += pattern_outputs
    #pretty print
    print(json.dumps(output, indent=4))
    output_f.write(json.dumps(output, indent=4))

def create_output(pattern, env):
  sink_output = {}
  for illegal_flow in env.illegal_flows:
    illegal_output = {}
    illegal_output['vulnerability'] = pattern['vulnerability']
    illegal_output['unsanitized flows'] = "no"
    illegal_output['sink'] = illegal_flow['sink']
    illegal_output['sanitized flows'] = []
    label = illegal_flow['label']
    for flow in label.flows:
      illegal_output['sanitized flows'] = []
      illegal_output['source'] = flow.source
      if flow.source in sink_output.keys():
        sink_output[flow.source]['sanitized flows'].append(flow.sanitizers)
      else:
        illegal_output['sanitized flows'].append(flow.sanitizers)
        sink_output[flow.source] = illegal_output.copy()
  for source, output in sink_output.items():
    if [] in output['sanitized flows']:
      output['unsanitized flows'] = "yes"
      output['sanitized flows'] = list(filter(None, output['sanitized flows']))
  return sink_output.values()
          

  #    return ast.eval(env, patterns)

eval()