from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFS(self, start, visited):
        visited[start] = True
        print(start, end=" ")

        for neighbor in self.graph[start]:
            if not visited[neighbor]:
                self.DFS(neighbor, visited)

    def performDFS(self, start):
        visited = [False] * self.vertices
        self.DFS(start, visited)

if __name__ == "__main__":
    g = Graph(8)
    g.addEdge(0, 1)
    g.addEdge(0, 3)
    g.addEdge(1, 2)
    g.addEdge(1, 4)
    g.addEdge(2, 5)
    g.addEdge(3, 6)
    g.addEdge(4, 7)
    g.addEdge(5, 7)

    start_vertex = 0
    print(f"Depth-First Traversal starting from vertex {start_vertex}:")
    g.performDFS(start_vertex)
