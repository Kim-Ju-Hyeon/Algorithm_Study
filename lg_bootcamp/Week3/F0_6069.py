import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    L = int(readl())
    N = int(readl())
    dist = [0] + list(map(int, readl().split()))
    time = [0] + list(map(int, readl().split())) + [0]
    return L, N, dist, time


# 입력받는 부분
L, N, dist, time = Input_Data()

# 여기서부터 작성