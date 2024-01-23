import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    matrix = [list(map(int, readl().split())) for _ in range(N)]
    return N, M, matrix


sol = -1
route = []
# 입력 받는 부분
N, M, matrix = Input_Data()

dist_list = [1e9] * N
visited = [False] * N
prev = [-1] * N

# 여기서부터 작성
def bfs():
    q = deque()
    q.append((0, 0))

    while q:
        cur_station, cur_dist = q.popleft()
        dist_list[cur_station] = cur_dist

        for next_station in range(N):
            if dist_list[next_station] > matrix[cur_station][next_station] + cur_dist:
                q.append((next_station, cur_dist + matrix[cur_station][next_station]))
                prev[next_station] = cur_station


bfs()
print(dist_list)
print(prev)
