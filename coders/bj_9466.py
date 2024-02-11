import sys

def input():
    return sys.stdin.readline()


T = int(input())
for _ in range(T):
    N = int(input())
    card_list = [list(map(int, input().split())) for _ in range(2)]

    if N == 1:
        print(max(card_list[0][0], card_list[1][0]))
        continue

    dp = [[0] * N for _ in range(2)]
    dp[0][0] = card_list[0][0]
    dp[1][0] = card_list[1][0]

    dp[0][1] = dp[1][0] + card_list[0][1]
    dp[1][1] = dp[0][0] + card_list[1][1]

    if N == 2:
        print(max(dp[0][1], dp[1][1]))
        continue

    for i in range(2, N):
        dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + card_list[0][i]
        dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + card_list[1][i]


    print(max(dp[0][-1], dp[1][-1]))