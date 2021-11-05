import Lab7
g = Lab7.Graph()
for i in range(7):
    g.addVertex(i)
g.addEdge(1, 4, 1)
g.addEdge(1, 2, 2)
g.addEdge(2, 4, 3)
g.addEdge(2, 5, 10)
g.addEdge(4, 3, 2)
g.addEdge(4, 6, 8)
g.addEdge(4, 7, 4)
g.addEdge(4, 5, 2)
g.addEdge(3, 6, 5)
g.addEdge(7, 6, 1)
g.addEdge(5, 7, 6)
g.addEdge(3, 1, 4)

list = g.shortest_path(g.vertList[1])



