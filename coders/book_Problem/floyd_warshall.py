import sys

'''
dummy input
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
'''

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())


distance_map = [[INF]*(n+1) for _ in range(n+1)]

# self-loop distance = 0
for i in range(n+1):
    for j in range(n+1):
        if i == j:
            distance_map[i][j] = 0

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

    # one step distance
    distance_map[a][b] = c


for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            distance_map[a][b] = min(distance_map[a][b], distance_map[a][k] + distance_map[k][b])

for i in range(1,n+1):
    print(distance_map[i][1:])