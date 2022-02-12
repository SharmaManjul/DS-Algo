class Graph:

  def __init__(self):
    self.numberofnodes = 0
    self.adjacentlist = {}

  def addVertex(self,node):
      if (node is not None) and (node not in self.adjacentlist):
          self.numberofnodes += 1
          self.adjacentlist[node] = []
      else:
          print("Input vertex is either None or already exists in graph.")
          return False

  def addEdge(self,node1,node2):
      if node1 in self.adjacentlist:
          self.adjacentlist[node1].append(node2)
          self.adjacentlist[node2].append(node1)

  def show_connections(self):
    for node in self.adjacentlist:
        print(f'{node} -->> {" ".join(map(str, self.adjacentlist[node]))}')


myGraph = Graph()
myGraph.addVertex('0')
myGraph.addVertex('1')
myGraph.addVertex('2')
myGraph.addVertex('3')
myGraph.addVertex('4')
myGraph.addVertex('5')
myGraph.addVertex('6')
myGraph.addEdge('3', '1')
myGraph.addEdge('3', '4')
myGraph.addEdge('4', '2')
myGraph.addEdge('4', '5')
myGraph.addEdge('1', '2')
myGraph.addEdge('1', '0')
myGraph.addEdge('0', '2')
myGraph.addEdge('6', '5')
print(myGraph)
myGraph.show_connections()
