import collections

class Graph: 
    def __init__(self): 
        self.graph = collections.defaultdict(list)

    def add_connections(self, vertexFrom, vertexTo): 
        self.graph[vertexFrom].append(vertexTo)
        self.graph[vertexTo].append(vertexFrom)


def shortestPath(graph, startVertex, targetVertex): 
    distances = dict()
    queue = collections.deque() 

    queue.append(startVertex)
    distances[startVertex] = 0 

    while queue: 
        currentVertex = queue.popleft()

        for vertex in graph[currentVertex]: 
            if vertex not in distances: 
                queue.append(vertex)
                distances[vertex] = distances[currentVertex] + 1

                if vertex == targetVertex: break 

    return distances[targetVertex]
    

# driver code
g = Graph()
g.add_connections(1, 2)
g.add_connections(1, 3) 
g.add_connections(2, 4)
g.add_connections(3, 5)
g.add_connections(4, 6)
g.add_connections(3, 4)

print(shortestPath(g.graph, 1, 6))

