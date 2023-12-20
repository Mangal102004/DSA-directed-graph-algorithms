from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, start):
        visited = [False] * self.vertices
        queue = deque()

        queue.append(start)
        visited[start] = True

        while queue:
            current_vertex = queue.popleft()
            print(current_vertex, end=" ")

            for neighbor in self.graph[current_vertex]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True


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

    print("Breadth-First Traversal starting from vertex 0:")
    g.BFS(0)
