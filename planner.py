import json
import heapq

def load_data():
    with open('data.json', 'r') as f:
        return json.load(f)

def find_route_with_penalty(data, start, end, penalty=5):
    graph = {stop: [] for stop in data['stops']}
    for route in data['routes']:
        graph[route['from']].append((route['to'], route['cost'], route['mode']))

    # PQ stores: (total_cost, current_node, path_history, last_mode)
    pq = [(0, start, [], None)]
    visited = {} # Using a dict to store the best cost to reach a node with a specific mode

    while pq:
        (cost, current, path, last_mode) = heapq.heappop(pq)

        # Optimization: skip if we've found a better way to this node with this mode
        if (current, last_mode) in visited and visited[(current, last_mode)] <= cost:
            continue
        visited[(current, last_mode)] = cost
        
        new_path = path + [current]

        if current == end:
            return cost, new_path

        for neighbor, weight, mode in graph.get(current, []):
            total_weight = weight
            
            # Apply penalty if mode changes (and it's not the first leg)
            if last_mode is not None and mode != last_mode:
                total_weight += penalty
                print(f"--- Transfer Penalty applied at {current} ({last_mode} -> {mode}) ---")

            heapq.heappush(pq, (cost + total_weight, neighbor, new_path, mode))

    return float("inf"), []

if __name__ == "__main__":
    transit_data = load_data()
    total_time, best_path = find_route_with_penalty(transit_data, "Central", "Airport")

    print("\n--- ADVANCED TRANSIT PLANNER (With Transfer Penalties) ---")
    print(f"Route: {' -> '.join(best_path)}")
    print(f"Total Time: {total_time} minutes")