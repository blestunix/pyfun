class Graph:
  def __init__(self, graph={}):
    self.graph = graph

  def find_path(self, start, end):
    q = [start]
    path = []
    while q:
      curr = q.pop(0)
      if curr == end or end in self.graph[curr]:
        return path
      path.append(curr)
      for connected in self.graph[curr]:
        if connected not in q and connected not in path:
          q.append(connected)
