import sys

def input():
    return sys.stdin.readline()


N = int(input())
snow = list(map(int, input().split()))

def solution():
    answer = 1e99
    snow.sort()
    for i in range(N-4):
        tmp = snow[i:i+4]
        snowman_1 = tmp[0] + tmp[-1]
        snowman_2 = tmp[1] + tmp[2]

        diff = abs(snowman_1 - snowman_2)
        answer = min(answer, diff)

    return answer 


print(solution())