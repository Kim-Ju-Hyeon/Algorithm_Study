import sys

input = sys.stdin.readline

N, M = map(int, input().split())

r, c, d = map(int, input().split())

graph = [[] for _ in range(N)]
for i in range(N):
    graph[i] = list(map(int, input().split()))

d_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def check_0_place(x, y):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if graph[nx][ny] == 0:
            return True
    return False


def solution(r, c, d):
    global count
    direc = d_list[d]

    while True:
        if graph[r][c] == 0:
            graph[r][c] = 2
            count += 1

        if check_0_place(r, c):
            for _ in range(4):
                d = (d + 3) % 4
                direc = d_list[d]
                nr, nc = r + direc[0], c + direc[1]

                if graph[nr][nc] == 0:
                    r, c = nr, nc
                    break
        else:
            nr, nc = r - direc[0], c - direc[1]
            r, c = nr, nc
            if graph[r][c] == 1:
                return count


count = 0
print(solution(r, c, d))
