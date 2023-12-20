class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def kruskal(self):
        result = []
        edges = []
        for i in range(self.V):
            for j in range(i+1, self.V):
                if self.graph[i][j] != 0:
                    edges.append([i, j, self.graph[i][j]])

        edges = sorted(edges, key=lambda item: item[2])
        parent = [i for i in range(self.V)]
        rank = [0] * self.V

        for u, v, w in edges:
            x = self.find_parent(parent, u)
            y = self.find_parent(parent, v)

            if x != y:
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        print("Edge \tWeight")
        for u, v, w in result:
            print(f"{u} - {v}\t{w}")

    def find_parent(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_parent(parent, parent[i])

    def union(self, parent, rank, x, y):
        root_x = self.find_parent(parent, x)
        root_y = self.find_parent(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y
            rank[root_y] += 1

if __name__ == '__main__':
    g = Graph(8)
    g.graph = [
        [0, 3, 0, 0, 0, 0, 0, 7],
        [3, 0, 7, 0, 0, 0, 0, 10],
        [0, 7, 0, 5, 0, 3, 0, 0],
        [0, 0, 5, 0, 8, 12, 0, 0],
        [0, 0, 0, 8, 0, 9, 0, 0],
        [0, 0, 3, 12, 9, 0, 4, 0],
        [0, 0, 0, 0, 0, 4, 0, 1],
        [7, 10, 0, 0, 0, 0, 1, 0]
    ]

    g.kruskal()
