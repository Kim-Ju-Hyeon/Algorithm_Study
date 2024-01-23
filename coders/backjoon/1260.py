import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    from_v, to_v = map(int, sys.stdin.readline().split())
    graph[from_v].append(to_v)
    graph[to_v].append(from_v)

for edge_list in graph:
    edge_list.sort()

visited = [False] * (N + 1)


def dfs(node):
    print(node, end=' ')
    visited[node] = True

    for new_node in graph[node]:
        if not visited[new_node]:
            dfs(new_node)

def bfs(start):
    queue = deque([start])
    visited[start] = True

    while queue:
        cur_node = queue.popleft()
        print(cur_node, end=' ')

        for new_node in graph[cur_node]:
            if not visited[new_node]:
                queue.append(new_node)
                visited[new_node] = True

dfs(V)
print()
visited = [False] * (N + 1)
bfs(V)