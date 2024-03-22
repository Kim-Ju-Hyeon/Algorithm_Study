import sys

def input():
    return sys.stdin.readline()

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

def solution():
    answer = 1e99

    end = 0
    interval_sum = 0

    for start in range(N):
        while interval_sum < S and end < N:
            interval_sum += numbers[end]
            end += 1


        if interval_sum >= S:
            answer = min(answer, end - start)
        interval_sum -= numbers[start]

    if answer == 1e99:
        return 0
    
    return answer

print(solution())
