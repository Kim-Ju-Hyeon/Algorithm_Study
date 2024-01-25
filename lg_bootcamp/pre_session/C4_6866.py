import sys
from bisect import bisect_left, bisect_right

def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    num = [0] + list(map(int, readl().split()))
    T = int(readl())
    query = list(map(int, readl().split()))
    return N, num, T, query


sol = []
# 입력받는 부분
N, num, T, query = Input_Data()

# 여기서부터 작성
for q in query:
    l = bisect_left(num, q)
    if num[l] != q:
        sol.append(0)
        continue
    r = bisect_right(num, q)
    sol.append(r-l)

# 출력하는 부분
print(*sol)
