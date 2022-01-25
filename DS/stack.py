class Stack:
  def __init__(self):
    self.items = []
  
  def push(self, item):
    self.items.append(item)
  
  def pop(self):
    self.items.pop()
    
  def peek(self):
    return self.items[-1]
  
  def is_empty(self):
    return len(self.items) == 0
  
  def display(self):
    print(self.items)
    
stk = Stack()
print(stk.is_empty())
stk.push(1)
stk.push(2)
stk.display()
stk.pop()
stk.display()
print(stk.peek())
print(stk.is_empty())
