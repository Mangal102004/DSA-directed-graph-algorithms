class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

    def minKey(self, key, mstSet):
        min_val = float('inf')
        min_index = 0

        for v in range(self.V):
            if key[v] < min_val and mstSet[v] is False:
                min_val = key[v]
                min_index = v

        return min_index

    def primMST(self):
        key = [float('inf')] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V
        parent[0] = -1

        for _ in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] is False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent)

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

    g.primMST()
