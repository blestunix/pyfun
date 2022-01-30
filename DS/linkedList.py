class Node:
  def __init__(self, val, nxt=None):
    self.val = val
    self.nxt = nxt

class LinkedList:
  def __init__(self):
    self.head = None
  
  def insertHead(self, data):
    self.head = Node(data, self.head)
    
  def insertTail(self, data):
    if self.head is None:
      return self.inserHead(data)
    trav = self.head
    while trav.nxt:
      trav = trav.nxt
    trav.nxt = Node(data)
  
  def removeHead(self):
    self.head = self.head.nxt
    
  def removeTail(self):
    if self.head:
      if self.head.nxt:
        trav = self.head
        while trav.nxt.nxt:
          trav = trav.nxt
        trav.nxt = None
      else:
        self.removeHead()
    else:
      print("LL has no head")

  def display(self):
    node = self.head
    print("*" * 25, "Current LL", "*" * 25)
    while node:
      print(node.val)
      node = node.nxt
    print("*" * 25, "   End    ", "*" * 25)
    print()
