N = int(input())

k = 0
while N % 3 == 0:
    N = N // 3
    k += 1

dp = {}
dp[0] = ["*"]

for i in range(1,k+1):
    dp[i] = []
    for r in range(3**i):
        if 3**(i-1) <= r < 3**(i-1)*2:
            dp[i].append(dp[i-1][r%(3**(i-1))] + ' '*3**(i-1) + dp[i-1][r%(3**(i-1))])
        else:
            dp[i].append(dp[i-1][r%(3**(i-1))]*3)


for i in range(len(dp[k])):
    print(dp[k][i])