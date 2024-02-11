import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    W = int(readl())
    pos = [list(map(int, readl().split())) for n in range(W)]
    return N, W, pos


# 입력받는 부분
N, W, pos = Input_Data()

# 여기서부터 작성
answer = [1e99]
p1 = (1, 1)
p2 = (N, N)


def dfs(idx, p1, p2, d):
    if d >= answer[0]:
        return

    if idx >= W:
        answer[0] = min(answer[0], d)
        return

    dfs(idx + 1, pos[idx], p2, d + abs(p1[0] - pos[idx][0]) + abs(p1[1] - pos[idx][1]))
    dfs(idx + 1, p1, pos[idx], d + abs(p2[0] - pos[idx][0]) + abs(p2[1] - pos[idx][1]))

dfs(0, p1, p2, 0)
# 출력하는 부분
print(answer[0])
