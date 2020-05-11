from collections import defaultdict 
class DirectedGraph: 
    def __init__(self): 
        self.graph = defaultdict(list)

    def add_connection(self, nodeFrom, nodeTo): 
        self.graph[nodeFrom].append(nodeTo)

def lowestCommonManager(topManager, reportOne, reportTwo, graph): 
    return countOccurences(topManager, reportOne, reportTwo, graph)['lowestCommon']

def countOccurences(node, reportOne, reportTwo, graph): 
    count = 0
    for reporter in graph[node]: 
        infoAtLevel = countOccurences(reporter, reportOne, reportTwo, graph) 
        count += infoAtLevel['countOccurences']
        if infoAtLevel['lowestCommon']: return infoAtLevel

    if node == reportOne or node == reportTwo: count += 1 

    manager = node if count == 2 else None 

    return {'lowestCommon': manager, 'countOccurences': count} 

    

# create graph 
graph = DirectedGraph()
graph.add_connection('A', 'B')
graph.add_connection('A', 'C')
graph.add_connection('B', 'D')
graph.add_connection('B', 'E')
graph.add_connection('D', 'H')
graph.add_connection('D', 'I')
graph.add_connection('C', 'F')
graph.add_connection('C', 'G')

print(lowestCommonManager('A', 'E', 'I', graph.graph))