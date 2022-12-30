def create_label(level, sources, sanitizers):
  return {
    "level": level, 
    "sources": sources, 
    "sanitizers": sanitizers
    }

def get_sources(lab):
  return lab["sources"]

def get_level(lab):
  return lab["level"]

def get_sanitizers(lab):
  return lab["sanitizers"]

def add_sanitizer(lab, sanitizer):
  lab["sanitizers"].add(sanitizer)

def is_bottom(lab):
  return get_level(lab) == "T"

def bottom(src):
  return create_label("T", set([src]), set())

def top():
  return create_label("UT", set(), set())

def glb(lab1, lab2):
  if is_bottom(lab1) and is_bottom(lab2):
    union_sources = get_sources(lab1).union(get_sources(lab2))
    union_sanitizers = get_sanitizers(lab1).union(get_sanitizers(lab2))
    return create_label("T", union_sources, union_sanitizers)
  elif is_bottom(lab1):
    return lab1  
  else:
    return lab2