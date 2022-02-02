class Tree:
    def __init__(self, val):
        self.data = val
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
   
