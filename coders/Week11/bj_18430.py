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

print(solution())