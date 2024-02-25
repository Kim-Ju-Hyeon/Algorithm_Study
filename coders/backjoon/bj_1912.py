import sys

def input():
    return sys.stdin.readline()

N = int(input())
num_list = list(map(int, input().split()))

def solution():
    stack = [0] * N
    # [10, 6, 9, 10, 15, 21, -35, 12, 33, 32]
    num_sum = 0

    for i, num in enumerate(num_list):
        new_sum = num_sum + num

        if new_sum < 0:
            stack[i] = num
            num_sum = 0
        else:
            stack[i] = new_sum
            num_sum = new_sum

    return max(stack)

def solution2():
    max_num = -1e99
    _temp = 0

    for num in num_list:
        _temp += num

        max_num = max(max_num, _temp)

        if _temp < 0:
            _temp = 0

    return max_num

def solution3():
    dp = [0] * N
    dp[0] = num_list[0]

    for i in range(1,N):
        dp[i] = max(dp[i-1]+num_list[i], num_list[i])

    return max(dp)


print(solution2())