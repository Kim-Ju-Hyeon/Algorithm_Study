import heapq

graph = {
    1: [(2, 2), (1, 4)],
    2: [(1, 3), (9, 5), (6, 6)],
    3: [(4, 6)],
    4: [(3, 3), (5, 7)],
    5: [(1, 8)],
    6: [(3, 5)],
    7: [(7, 6), (9, 8)],
    8: []
}

costs = {}
prev = {}

def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    costs[start] = 0
    prev[start] = None  # The start node has no previous node

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)
        if cur_node in costs and cur_cost > costs[cur_node]:
            continue
        for cost, next_node in graph[cur_node]:
            next_cost = cur_cost + cost
            if next_node not in costs or next_cost < costs[next_node]:
                costs[next_node] = next_cost
                prev[next_node] = cur_node
                heapq.heappush(pq, (next_cost, next_node))

dijkstra(1)

# If you want to get the path from the start to a certain node, you can do the following:
end = 8  # Let's say we want to get the path from the start to node 6
path = []
while end is not None:
    path.append(end)
    end = prev[end]
path = path[::-1]  # Reverse the path

print(path)
print(prev)