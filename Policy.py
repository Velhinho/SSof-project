def get_sec_classes():
  return {"T", "UT"}

def glb(lab1, lab2):
  return lab1 if lab1["level"] == "T" else lab2

def lub(lab1, lab2):
  return lab1 if lab1["level"] == "UT" else lab2

def is_bottom(lab):
  return lab["level"] == "T"

def get_source(lab):
  return lab["source"]

def bottom(src):
  return {"level": "T", "source": src}

def top():
  return {"level": "UT", "source": None}