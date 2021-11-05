import queue


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}  # stores connected label as a key then the path weight

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}  # saves vertex in a dict where key is the id and item is vertex
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def shortest_path(self, vertex):
        path_table = [[] for n in range(self.numVertices - 1)]
        z = 0
        for n in range(self.numVertices - 1):  # initialize table
            if z + 1 == vertex.id:  # initialize the first vertex zero/ z-1 is bc index start with 0
                path_table[z] = [vertex.id, False, 0, 0]  # [vertex num, known, path weight, parent]
            else:
                path_table[z] = [z + 1, False, 100000, 0]
            z += 1
        path_queue = queue.QueuekLinkedList(100)  # initialize size with 100
        spacer = "hehe"
        path_queue.enqueue(vertex)
        path_queue.enqueue(spacer)
        while path_queue.size() > 0:
            rooty = path_queue.dequeue()
            if rooty != spacer:
                path_table[rooty.id - 1][1] = True  # set known to True so it wont be repeated
                if rooty != None:

                    for k in rooty.connectedTo.keys():  # puts the connected vertex into queue
                        if path_table[k.id - 1][1] != True:
                            path_queue.enqueue(k)
                        path_length = path_table[rooty.id - 1][2] + rooty.connectedTo[k]
                        if path_length < path_table[k.id - 1][2]:  # if path is shorter then replace parent and weight
                            path_table[k.id - 1][2] = path_length
                            path_table[k.id - 1][3] = rooty
            else:
                if path_queue.is_empty():
                    break
        self.shortest_path_helper(path_table)
        return path_table

    def shortest_path_helper(self, path_table): # prints it in the correct format
        listy = []
        for x in range(len(path_table)):
            listy2 = self.shortest_path_helper_helper(path_table, x)    # x is the index of vertex in path table
            listy3 =['V' + str(path_table[x][0]), listy2, path_table[x][2]]
            listy.append(listy3)
        print(listy)

    def shortest_path_helper_helper(self, path_table, x): # get a listy of how to get there
        listy = []
        if x != 0:
            listy.append('V' + str(path_table[x][0]))
            temp = x
            while True: # if temp.parent is not 0
                if path_table[temp][3] != 0:
                    temp = path_table[temp][3].id - 1
                    listy.append('V' + str(path_table[temp][0]))
                else:
                    break
        rev_list = listy[::-1]
        return rev_list


