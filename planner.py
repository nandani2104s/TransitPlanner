import json
import heapq

# 1. Load the data
def load_data():
    with open('data.json', 'r') as f:
        return json.load(f)

# 2. The Core Algorithm
def find_route(data, start, end):
    # Adjacency List: { 'StopA': [('StopB', cost, mode), ...] }
    graph = {stop: [] for stop in data['stops']}
    for route in data['routes']:
        graph[route['from']].append((route['to'], route['cost'], route['mode']))

    # Priority Queue stores: (total_cost, current_node, path_history)
    # heapq always pops the SMALLEST cost (Greedy Choice)
    pq = [(0, start, [])]
    visited = set()

    while pq:
        (cost, current, path) = heapq.heappop(pq)

        if current in visited:
            continue
        
        path = path + [current]
        visited.add(current)

        # Goal Reached
        if current == end:
            return cost, path

        # Explore neighbors
        for neighbor, weight, mode in graph.get(current, []):
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor, path))

    return float("inf"), []

# 3. Run the Program
if __name__ == "__main__":
    transit_data = load_data()
    total_time, best_path = find_route(transit_data, "Central", "Airport")

    print("--- TRANSIT PLANNER ---")
    print(f"Start: Central | Destination: Airport")
    print(f"Optimal Path: {' -> '.join(best_path)}")
    print(f"Estimated Time: {total_time} minutes")