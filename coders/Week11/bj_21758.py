import sys

def input():
    return sys.stdin.readline()


N = int(input())
line = list(map(int, input().split()))

def solution():
    answer = 0

    # case 1
    for i in range(1, N-1):
        bee_1 = sum(line[1:i+1])
        bee_2 = sum(line[i:N-1])

        answer = max(answer, bee_1+bee_2)

    # case 2
    for i in range(1, N - 1):
        bee_1 = sum(line[1:]) - line[i]
        bee_2 = sum(line[i+1:])

        answer = max(answer, bee_1 + bee_2)

    # case 3
    for i in range(1, N - 1):
        bee_1 = sum(line[:N-1]) - line[i]
        bee_2 = sum(line[:i])

        answer = max(answer, bee_1 + bee_2)

    return answer


# prefix sum
def solution2():
    answer = 0

    prefix_sum = [0] * N
    prefix_sum[0] = line[0]

    for i in range(1,N):
        prefix_sum[i] = prefix_sum[i-1] + line[i]

    # case 1 - move honey, fix bees
    for i in range(1, N-1):
        bee_1 = prefix_sum[i] - prefix_sum[0]
        bee_2 = prefix_sum[N-1-1] - prefix_sum[i-1]

        answer = max(answer, bee_1+bee_2)

    # case 2 - fix left bee, right honey
    for i in range(1, N - 1):
        bee_1 = prefix_sum[-1] - line[i] - line[0]
        bee_2 = prefix_sum[-1] - prefix_sum[i]

        answer = max(answer, bee_1 + bee_2)
    
    # case 3 - fix left honey, right bee
    for i in range(1, N - 1):
        bee_1 = prefix_sum[-1] - line[i] - line[-1]
        bee_2 = prefix_sum[i-1]

        answer = max(answer, bee_1 + bee_2)

    return answer


print(solution2())