def create_label(level, sources):
  return {"level": level, "sources": sources}

def get_sources(lab):
  return lab["sources"]

def get_level(lab):
  return lab["level"]

def glb(lab1, lab2):
  if is_bottom(lab1) and is_bottom(lab2):
    return create_label("T", lab1["sources"].union(lab2["sources"]))
  elif is_bottom(lab1):
    return lab1  
  else:
    return lab2

def is_bottom(lab):
  return lab["level"] == "T"

def bottom(src):
  return create_label("T", set([src]))

def top():
  return create_label("UT", set())