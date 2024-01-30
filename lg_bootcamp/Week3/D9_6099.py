import sys
from bisect import bisect_left

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    list_file = list(map(int, readl().split()))
    return N, list_file


# 입력받는 부분
N, list_file = Input_Data()


def solution():
    count = 0
    list_file.sort()

    for j, F_j in enumerate(list_file):
        lower = 0.9 * F_j
        left = bisect_left(list_file, lower)

        count += (j - left)

    return count

print(solution())