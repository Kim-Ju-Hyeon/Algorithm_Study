import sys
from collections import deque
from heapq import heapify, heappush, heappop

def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    matrix = [list(map(int, readl().split())) for _ in range(N)]
    return N, M, matrix


sol = -1
route = []
# 입력 받는 부분
N, M, matrix = Input_Data()

# 여기서부터 작성
