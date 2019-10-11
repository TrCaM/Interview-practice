class Node:
  def __init__(self, x: int):
    self.val = x


class Graph:
  def __init__(self):
    """
    Using adjacency list
    """
    self.adjacentList = {}
  
  def addNode(self, node):
    self.adjacentList[node] = set()

  def addNodes(self, *args):
    for v in args:
      self.adjacentList[Node(v)] = set()
  
  def getNodes(self):
    return list(self.adjacentList.keys())

  def addEdge(self, v1, v2):
    if v1 not in self.adjacentList or v2 not in self.adjacentList:
      raise Exception("This is bad")
    self.adjacentList[v1].add(v2)
    self.adjacentList[v2].add(v1)
  
  def deleteNode(self, node):
    if node in self.adjacentList.keys():
      adjNodes = self.adjacentList[node]
      for adj in adjNodes:
        self.adjacentList[adj].remove(node)
      del self.adjacentList[node]
    return node 
  
  def deleteEdge(self, v1, v2):
    if v1 not in self.adjacentList or v2 not in self.adjacentList:
      raise Exception("This is bad")
      
    self.adjacentList[v1].remove(v2)
    self.adjacentList[v2].remove(v1)
  
  def printGraph(self):
    for node, adjList in self.adjacentList.items():
      print(f"Node {node.val}: {[v.val for v in adjList]}")

  def traverse(self):
    visisted = set()
    def dfs(node):
      if node in visisted:
        return
      visisted.add(node)
      print(node.val)
      for adjacent in self.adjacentList[node]:
        dfs(adjacent) 
    
    def dfs_iter(node):
      stack = [node]
      while len(stack) > 0:
        print([n.val for n in stack])
        cur = stack.pop()
        if cur in visisted:
          continue
        visisted.add(cur)
        print(cur.val)
        stack += list(self.adjacentList[cur])
    
    def bfs(node):
      queue = [node]
      while len(queue) > 0:
        print([n.val for n in queue])
        cur = queue.pop()
        if cur in visisted:
          continue
        visisted.add(cur)
        print(cur.val)
        queue = list(self.adjacentList[cur]) + queue



    for node in self.adjacentList.keys():
      bfs(node)
    



G = Graph()
G.addNodes(0, 1, 2, 3, 4, 5, 6, 7)
nodes = G.getNodes()
G.printGraph()
# print([node.val for node in nodes])
G.addEdge(nodes[0], nodes[1])
G.addEdge(nodes[1], nodes[2])
G.addEdge(nodes[2], nodes[3])
G.addEdge(nodes[3], nodes[4])
G.addEdge(nodes[4], nodes[0])
G.addEdge(nodes[4], nodes[2])
G.addEdge(nodes[0], nodes[6])
G.addEdge(nodes[5], nodes[7])
G.printGraph()
print()

G.traverse()
# G.deleteNode(nodes[4])
# G.printGraph()