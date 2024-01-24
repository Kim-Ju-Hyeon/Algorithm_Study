import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    map_uv = [list(map(int, readl().strip())) for _ in range(N)]
    return N, map_uv


sol = -1
# 입력 받는 부분
N, map_uv = Input_Data()

# 여기서부터 작성
