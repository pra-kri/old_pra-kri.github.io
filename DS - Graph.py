# implementation of a graph in Python.

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbour(self, neybr, weight = 0):
        self.connectedTo[neybr] = weight

    def __str__(self):
        return str(self.id) + 'connected to' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getID(self):
        return self.id

    def getWeight(self, neybr):
        return self.connected[neybr]


# second class: the actual graph, which contains many vertices...


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n): #overload the contains function....
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbour(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


# OK graph and vertices implemented fully so far.
# now need to actually create a graph and test it to see if it works...


g = Graph()

for i in range(11):
    g.addVertex(i)

print(g.vertList)
#works up to here


g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,3)
g.addEdge(2,3,9)
g.addEdge(3,5,7)
g.addEdge(6,8,1)
g.addEdge(9,1,2)


for x in g:
    for y in x.getConnections():
        print("( %s , %s)" % (x.getID(), y.getID()))
