from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        '''
        @vertices: number of vertices
        '''
        self.graph = defaultdict(list) # adjacency list
        self.V = vertices
    

    def addEdge(self, u, v):
        self.graph[u].append(v)


    def topologicalSort(self):
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if not visited[i]:
                self.topologicalUtil(i, visited, stack)

        return stack
    

    def topologicalUtil(self, i, visited, stack):
        visited[i] = True

        for j in self.graph[i]:
            if not visited:
                self.topologicalUtil(j, visited, stack)
        
        stack.append(i)


if __name__ == '__main__':
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(2, 3)
    g.addEdge(3, 1)

    print(g.topologicalSort())