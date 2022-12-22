class Environment:
    def __init__(self, pattern):
        self.pattern = pattern
        self.indentation = 0
        self.labenv = {}
        self.sources = []
        for source in pattern["sources"]:
            self.sources.append(source)
            self.labenv[source] = "T"
        self.sinks = pattern["sinks"]
        self.implicit = pattern["implicit"] == "yes"
        # stores context
        self.pc = "UT"

    def get_level(self, variable):
        return self.labenv[variable]

    def allow_implicit(self):
        return self.implicit