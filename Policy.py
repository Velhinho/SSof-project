class TUTPolicy():

    def get_sec_classes(self):
        return {"T", "UT"}

    def glb(self, lab1, lab2):
        if lab1=="T" or lab2=="T":
            return "T"
        else:
            return "UT"

    def lub(self, lab1, lab2):
        if lab1=="UT" or lab2=="UT":
            return "UT"
        else:
            return "T"

    def bottom(self):
        return "T"

    def top(self):
        return "UT"