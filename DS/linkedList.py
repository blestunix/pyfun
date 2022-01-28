class Node:
  def __init__(self, val, nxt=None):
    self.val = val
    self.nxt = nxt

class LinkedList:
  def __init__(self):
    self.head = None
  
  def insertHead(data):
    self.head = Node(data, self.head)
    
  def insertTail(data):
    if self.head is None:
      return self.inserHead(data)
    trav = self.head
    while trav.next:
      trav = trav.nxt
    trav.next = Node(data)
    
