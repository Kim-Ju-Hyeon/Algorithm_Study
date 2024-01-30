import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    info = [list(map(int, readl().split())) for _ in range(N)]
    return N, info


# 입력받는 부분
N, info = Input_Data()

# 여기서부터 작성
def check(mid):
    c = 0 # 왼쪽 마을에서 넘어온 수
    for i in range(N-1):
        remain = info[i][1] + c - mid # 남은 물고기의 수
        c = remain - (info[i+1][0] - info[i][0]) # 오른쪽 마을에 넘겨줄 물고기 수
        if remain > 0 and c < 0:
            c = 0
    return info[N-1][1] + c >= mid


def solution():
    s, e = 0, max(info, key=lambda x: x[1])[1]

    while s <= e:
        mid = (s + e) // 2

        if check(mid):
            sol = mid
            s = mid + 1
        else:
            e = mid - 1

    return sol


# 출력하는 부분
print(solution())