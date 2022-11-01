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

        for edge in range(self.V):
            pass
    
    def topologicalUtil(self, visited):
        visited[]
            