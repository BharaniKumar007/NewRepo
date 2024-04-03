import heapq

def calculate_distances(graph, starting_vertex, num_vertices, vertex_costs):
    distances = {vertex: float('infinity') for vertex in range(num_vertices)}
    distances[starting_vertex] = vertex_costs[starting_vertex]
    priority_queue = [(vertex_costs[starting_vertex], starting_vertex)]
    while len(priority_queue) > 0:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight + vertex_costs[neighbor]

            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        num_vertices = int(file.readline())
        num_edges = int(file.readline())
        graph = [{} for i in range(num_vertices)]

        vertex_costs = [float(file.readline()) for i in range(num_vertices)]
        for i in range(num_edges):
            a, b, c = file.readline().split()
            graph[int(a)-1][int(b)-1] = float(c)

    result = calculate_distances(graph, 4, num_vertices, vertex_costs)
    for i in result:
        print(i+1, ": ", result[i])
