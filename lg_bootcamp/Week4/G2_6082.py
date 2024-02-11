import sys
from copy import deepcopy


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    cost = [[0] + list(map(int, readl().split())) if 1 <= n <= N else [0] * (N + 1) for n in range(N + 1)]
    return N, cost


# 입력받는 부분
N, cost = Input_Data()


# 여기서부터 작성
def solution():
    answer = [1e99, []]
    visited = [False] * (N + 1)
    stack = []

    def dfs(idx, sum_cost):
        if idx == N:
            if answer[0] > sum_cost:
                answer[0] = sum_cost
                answer[1] = deepcopy(stack)
            return

        if sum_cost >= answer[0]:
            return

        for i in range(1, N + 1):
            if not visited[i]:
                visited[i] = True
                stack.append(i)
                dfs(idx + 1, sum_cost+cost[idx+1][i])
                visited[i] = False
                stack.pop()

    dfs(0, 0)
    print(answer[0])
    print(*answer[1])


solution()
