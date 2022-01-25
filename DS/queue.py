class Queue:
  def __init__(self):
    self.items = []
  
  def enqueue(self, item):
    self.items.append(item)
    
  def dequeue(self):
    self.items.pop(0)
   
  def front(self):
    return self.items[0]
  
  def back(self):
    return self.items[-1]
  
  def is_empty(self):
    return len(self.items) == 0
  
  def display(self):
    print(self.items)

q = Queue()
q.enqueue(1)
print(q.front(), q.back())
q.display()
q.enqueue('b')
print(q.front(), q.back())
q.dequeue()
q.display()
