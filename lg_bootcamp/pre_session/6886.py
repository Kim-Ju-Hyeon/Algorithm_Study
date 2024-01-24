import sys
from collections import deque
from heapq import heapify, heappush, heappop


def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    matrix = [list(map(int, readl().split())) for _ in range(N)]
    return N, M, matrix


# 입력 받는 부분
N, M, matrix = Input_Data()

distance = [1e99] * (N+1)
prev_station_list = [0] * (N+1)

# 여기서부터 작성
def bfs():
    pq = []
    heappush(pq, (0, 1)) # (dist, station)
    distance[0] = 0
    iter = 0

    while pq:
        print(pq)
        print(distance)
        print(prev_station_list)
        cur_dist, cur_station = heappop(pq)

        if distance[cur_station] <= cur_dist:
            continue

        for next_station in range(1, N+1):
            ndist = cur_dist + matrix[cur_station-1][next_station-1]

            if distance[next_station] <= ndist:
                continue

            heappush(pq, (ndist, next_station))
            distance[next_station] = ndist
            prev_station_list[next_station] = cur_station

        iter += 1

        if iter == 30:
            return
bfs()
print(distance)
print(prev_station_list)
