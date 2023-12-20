class Directed_Graph():

    def __init__(self, num_vertices):
        self.V = num_vertices
        self.adj_matrix = [[0 for _ in range(num_vertices)]
                          for _ in range(num_vertices)]

    def print_result(self, distances):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t\t", distances[node])

    def find_min_distance(self, distances, visited_set):
        min_dist = float('inf')
        min_index = -1

        for v in range(self.V):
            if distances[v] < min_dist and not visited_set[v]:
                min_dist = distances[v]
                min_index = v

        return min_index

    def dijkstra_algorithm(self, source):
        distances = [float('inf')] * self.V
        distances[source] = 0
        visited_set = [False] * self.V

        for _ in range(self.V):
            u = self.find_min_distance(distances, visited_set)
            visited_set[u] = True

            for v in range(self.V):
                if (self.adj_matrix[u][v] > 0 and not visited_set[v] and
                        distances[v] > distances[u] + self.adj_matrix[u][v]):
                    distances[v] = distances[u] + self.adj_matrix[u][v]

        self.print_result(distances)

    def find_shortest_path(self, source, destination):
        distances = [float('inf')] * self.V
        distances[source] = 0
        visited_set = [False] * self.V

        for _ in range(self.V):
            u = self.find_min_distance(distances, visited_set)
            visited_set[u] = True

            for v in range(self.V):
                if (self.adj_matrix[u][v] > 0 and not visited_set[v] and
                        distances[v] > distances[u] + self.adj_matrix[u][v]):
                    distances[v] = distances[u] + self.adj_matrix[u][v]

        path = []
        current_vertex = destination
        while current_vertex != source:
            path.insert(0, current_vertex)
            current_vertex = self.get_previous_vertex(distances, source, current_vertex)

        path.insert(0, source)
        print(f"Shortest Path from {source} to {destination}: {path}")

    def get_previous_vertex(self, distances, source, current_vertex):
        for v in range(self.V):
            if self.adj_matrix[v][current_vertex] > 0:
                if distances[current_vertex] == distances[v] + self.adj_matrix[v][current_vertex]:
                    return v

direc_g = Directed_Graph(8)
direc_g.adj_matrix = [
    [0, 3, 0, 0, 0, 0, 0, 7],
    [3, 0, 7, 0, 0, 0, 0, 10],
    [0, 7, 0, 5, 0, 3, 0, 0],
    [0, 0, 5, 0, 8, 12, 0, 0],
    [0, 0, 0, 8, 0, 9, 0, 0],
    [0, 0, 3, 12, 9, 0, 4, 0],
    [0, 0, 0, 0, 0, 4, 0, 1],
    [7, 10, 0, 0, 0, 0, 1, 0]
]

direc_g.dijkstra_algorithm(0)
direc_g.find_shortest_path(0, 6)  # Example: Find shortest path from vertex 0 to 6
