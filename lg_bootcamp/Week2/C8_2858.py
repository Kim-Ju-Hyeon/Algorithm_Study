import sys


def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    info = [list(map(int, readl().split())) for _ in range(N)]
    return N, info


sol = 0

# 입력받는 부분
N, info = input_data()

paper = [[0] * 102 for _ in range(102)]

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

# 여기서부터 작성
def check_corner(rr, cc):
    direc = []
    if paper[rr][cc] == 0:
        return False

    for i in range(4):
        nr = rr + dr[i]
        nc = cc + dc[i]
        if paper[nr][nc] == 0:
            direc.append((nr, nc))
    if len(direc) == 2:
        return direc
    else:
        return False

def solution():
    for c, r in info:
        for i in range(c, c + 10):
            for j in range(r, r + 10):
                paper[i][j] = 1

    for row in range(100):
        for col in range(100):
            if paper[row][col] == 1:
                for i in range(4):
                    nr = row + dr[i]
                    nc = col + dc[i]



    return edge