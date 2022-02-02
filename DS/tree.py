class Tree:
    def __init__(self, val):
        self.data = val
        self.children = []
        self.parent = None

    def add_child(self, child, duplicates_allowed=True):
        if not duplicates_allowed:
            if child in self.children:
                return
        child.parent = self
        self.children.append(child)
    
        def display(self):
        # bfs
        q = [self]

        while q:
            curr = q.pop(0)
            print(curr.data, end='\t')
            q.extend(curr.children)
        print('\n')
            
