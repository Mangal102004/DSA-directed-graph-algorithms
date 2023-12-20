V = 5
INF = float('inf')

def floydWarshall(graph):
    dist = [list(row) for row in graph]

    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    printSolution(dist)

def printSolution(dist):
    print("Shortest distances between every pair of vertices:")
    for i in range(V):
        for j in range(V):
            if dist[i][j] == INF:
                print("INF", end=" ")
            else:
                print(dist[i][j], end=" ")
        print()

if __name__ == "__main__":
    graph = [
        [0, 1, INF, 3, INF],
        [INF, 0, INF, 6, INF],
        [INF, INF, 0, INF, INF],
        [INF, INF, 2, 0, 1],
        [INF, INF, INF, INF, 0]
    ]

    floydWarshall(graph)
