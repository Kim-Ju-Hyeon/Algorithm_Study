import sys


def input_data():
    readl = sys.stdin.readline
    N = int(readl())
    weight = [int(readl()) for _ in range(N)]
    return N, weight


sol = -1
# 입력받는 부분
N, weight = input_data()

def solution():
    answer = [-1]

    def check(prev_weight, new_weight):
        min_length = len(str(min(prev_weight, new_weight)))
        for i in range(-1, -min_length-1, -1):
            temp = int(str(prev_weight)[i]) + int(str(new_weight)[i])
            if temp >= 10:
                return False
        return True

    def dfs(start, sum_weight, count):
        answer[0] = max(answer[0], count)

        if answer[0] > N - start + count:
            return

        for i in range(start, N):
            if check(sum_weight, weight[i]):
                dfs(i + 1, sum_weight + weight[i], count+1)

    dfs(0, 0, 0)
    print(answer[0])


solution()