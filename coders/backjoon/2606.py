import sys
from collections import deque

def input():
    return sys.stdin.readline()

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [False] * (N+1)
def bfs(start):
    answer = 0
    queue = deque([start])
    visited[start] = True

    while queue:
        cur_com = queue.popleft()
        for new_com in graph[cur_com]:
            if not visited[new_com]:
                queue.append(new_com)
                visited[new_com] = True
                answer += 1

    print(answer)

bfs(1)