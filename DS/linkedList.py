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
  
  def display(self):
    node = self.head
    while node:
      print(node.val)
      node = node.nxt
    
