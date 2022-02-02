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
            
'''
                                      Apple
                    /                   |                   \
               Products             Services         O p e r a t i n g   S y s t e m s
        /          |        \       /     \           |       |       |       |
      iPad      iPhone      Mac   Music   TV         iOS    macOS   iPadOS  watchOS
'''

apple = Tree("Apple")

products = Tree("Prodcuts")
ipad = Tree("iPad")
iphone = Tree("iPhone")
mac = Tree("Mac")
products.add_child(ipad)
products.add_child(iphone)
products.add_child(mac)

services = Tree("Services")
music = Tree("Music")
tv = Tree("TV")
services.add_child(music)
services.add_child(tv)

os = Tree("Operating Systems")
ios = Tree("iOS")
macos = Tree("macOS")
ipados = Tree("iPadOS")
watchos = Tree("watchOS")
os.add_child(ios)
os.add_child(macos)
os.add_child(ipados)
os.add_child(watchos)

apple.add_child(products)
apple.add_child(services)
apple.add_child(os)
apple.display()

os.display()
products.display()
