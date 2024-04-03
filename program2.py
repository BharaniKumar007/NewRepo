import heapq
import sys

# Function to read the input from a file and build the graph
# Function to read the input from a file and build the graph
def read_input(filename):
    with open(filename, 'r') as file:
        n = int(file.readline())
        m = int(file.readline())
        vertex_costs = [float(file.readline()) for _ in range(n)]
        graph = [[] for _ in range(n)]
        for _ in range(m):
            a, b, c = map(int, file.readline().split())
            graph[a - 1].append((b - 1, c))
        s = int(file.readline()) - 1
    return n, vertex_costs, graph, s


# Dijkstra's algorithm with vertex costs
def shortest_paths(graph, vertex_costs, s):
    n = len(graph)
    cost = [float('inf')] * n
    cost[s] = vertex_costs[s]
    min_heap = [(cost[s], s)]

    while min_heap:
        v_cost, v = heapq.heappop(min_heap)

        if v_cost > cost[v]:
            continue

        for u, edge_cost in graph[v]:
            new_cost = cost[v] + edge_cost + vertex_costs[u]
            if new_cost < cost[u]:
                cost[u] = new_cost
                heapq.heappush(min_heap, (cost[u], u))

    return cost

# Main function to process the input and display the output
def main(filename):
    n, vertex_costs, graph, s = read_input(filename)
    cost = shortest_paths(graph, vertex_costs, s)
    print(*cost)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python program2.py input.txt")
        sys.exit(1)
    input_filename = sys.argv[1]
    main(input_filename)
