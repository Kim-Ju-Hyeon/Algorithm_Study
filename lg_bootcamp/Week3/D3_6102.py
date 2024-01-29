import sys
from collections import deque

def Input_Data():
    readl = sys.stdin.readline
    N, K = map(int,readl().split())
    names = [readl().strip() for _ in range(N)]
    return N, K, names

sol = -1

# 입력 받는 부분
N, K, names = Input_Data()

# 여기서부터 작성
def solution_1():
    count = 0
    for i in range(N-1):
        for j in range(i+1, min(N,i+K+1)):
            if len(names[i]) == len(names[j]):
                count += 1
    return count

def solution_2():
    hash = {}
    count = 0

    for i, name in enumerate(names):
        if len(name) not in hash:
            hash[len(name)] = deque([i])
        else:
            while hash[len(name)] and abs(hash[len(name)][0] - i) > K:
                hash[len(name)].popleft()
            else:
                count += len(hash[len(name)])
                hash[len(name)].append(i)

    return count

# 출력하는 부분
print(solution_2())