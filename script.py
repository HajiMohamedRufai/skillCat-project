import heapq  # Importing the heapq module to use the priority queue


def dijkstra(graph, start):
    # Initialize the priority queue with the start node and distance 0
    priority_queue = [(0, start)]
    # Dictionary to store the shortest path to each node
    shortest_paths = {start: (None, 0)}
    # Set to keep track of visited nodes
    visited = set()

    while priority_queue:
        # Pop the node with the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)

        # If the node has been visited, skip it
        if current_node in visited:
            continue

        # Mark the node as visited
        visited.add(current_node)

        # Iterate over the neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If the neighbor has not been visited or a shorter path is found
            if neighbor not in shortest_paths or distance < shortest_paths[neighbor][1]:
                # Update the shortest path to the neighbor
                shortest_paths[neighbor] = (current_node, distance)
                # Push the neighbor to the priority queue
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_paths


# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
shortest_paths = dijkstra(graph, start_node)
print(shortest_paths)
