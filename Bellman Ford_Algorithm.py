class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def printArr(self, dist, parent):
        print("Vertex    Distance from Source         Optimal Path")
        for i in range(self.V):
            print("{0}\t\t\t\t\t{1}\t\t\t\t\t".format(i, dist[i]), end="")
            self.print_path(parent, i)
            print()

    def print_path(self, parent, j):
        if parent[j] == -1:
            print(j, end="")
            return
        self.print_path(parent, parent[j])
        print(" ->", j, end="")

    def BellmanFord(self, src):
        dist = [float("Inf")] * self.V
        dist[src] = 0
        parent = [-1] * self.V

        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    parent[v] = u

        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graph contains negative weight cycle")
                return

        self.printArr(dist, parent)

if __name__ == '__main__':
    g = Graph(5)
    g.addEdge(0, 1, -1)
    g.addEdge(0, 2, 4)
    g.addEdge(1, 2, 3)
    g.addEdge(1, 3, 2)
    g.addEdge(1, 4, 2)
    g.addEdge(3, 2, 5)
    g.addEdge(3, 1, 1)
    g.addEdge(4, 3, -3)

    g.BellmanFord(0)
