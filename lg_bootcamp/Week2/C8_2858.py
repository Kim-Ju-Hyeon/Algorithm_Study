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
def solution():
    for c, r in info:
        for i in range(c, c + 10):
            for j in range(r, r + 10):
                paper[j][i] = 1

    for row in range(102):
        for col in range(102):
            if paper[row][col] == 1:
                paper[row][col] = paper[row-1][col] + 1

    max_area = 0
    for row in range(102):
        for sc in range(102):
            height = 1e99
            if paper[row][sc] == 0:
                continue
            for ec in range(sc, 102):
                height = min(height, paper[row][ec])
                if height == 0:
                    break
                area = height * (ec - sc + 1)
                max_area = max(area, max_area)
    return max_area

print(solution())