import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    M, T, N = map(int, readl().split())
    info = [list(readl().split()) for _ in range(N)]
    info = [[i, int(s[0]), s[1]] for i, s in enumerate(info)]
    return M, T, N, info


M, T, N, info = Input_Data()


# 여기서 부터 작성
def solution():
    pass