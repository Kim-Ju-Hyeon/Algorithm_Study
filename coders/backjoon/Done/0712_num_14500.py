import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[0] for _ in range(N)]
for i in range(N):
    graph[i] = list(map(int, input().split()))

box_1 = [(0, 0), (1, 0), (0, 1), (1, 1)]
box_2 = [(0, 0), (1, 0), (2, 0), (3, 0)]
box_3 = [(0, 0), (0, 1), (1, 1), (1, 2)]
box_4 = [(0, 0), (0, 1), (-1, 1), (0, 2)]
box_5 = [(0, 0), (1, 0), (1, 1), (1, 2)]

techromino = [box_1, box_2, box_3, box_4, box_5]

answer = 0
for row in range(N):
    for col in range(M):
        for num in range(5):
            box = techromino[num]
            for symmetric in range(2):
                box = [(-x, y) for (x, y) in box]
                for rotate in range(4):
                    box = [(-y, x) for (x, y) in box]
                    summation = 0
                    for dxdy in box:
                        nrow, ncol = row + dxdy[0], col + dxdy[1]

                        if nrow < 0 or nrow >= N or ncol <0 or ncol >= M:
                            summation = int(-1e9)
                            break

                        summation += graph[nrow][ncol]
                    answer = max(answer, summation)

print(answer)