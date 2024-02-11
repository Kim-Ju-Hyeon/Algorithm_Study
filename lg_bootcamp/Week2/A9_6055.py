import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    num = [float(readl()) for _ in range(N)]
    return N, num

sol = 0.0
# 입력받는 부분
N, num = Input_Data()

# 여기서부터 작성
def solution_1():
    max_mul = -1
    for i in range(N):
        temp = num[i]
        for j in range(i+1, N):
            temp *= num[j]
            max_mul = max(max_mul, temp)
    return max_mul

def solution_2():
    dp = [n for n in num]
    for i in range(1, N):
        dp[i] = max(dp[i], dp[i-1]*dp[i])
    return max(dp)

sol = solution_2()

# 출력하는 부분
print(f"{sol:.3f}")