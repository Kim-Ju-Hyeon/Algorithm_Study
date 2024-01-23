import heapq
import sys

'''
dummy input
6 11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

start = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])

distance = [INF] * (n + 1)

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (distance[start], start))

    while q:
        dist, cur_node = heapq.heappop(q)
        if distance[cur_node] < dist:
            continue

        for node, length in graph[cur_node]:
            cost = dist + length
            if distance[node] > cost:
                distance[node] = cost
                heapq.heappush(q, (distance[node], node))

dijkstra(start)
print(distance)