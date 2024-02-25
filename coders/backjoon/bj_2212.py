import sys

def input():
    return sys.stdin.readline()


N = int(input())
K = int(input())
sensor_list = list(map(int, input().split()))

def solution(N, K, sensor_list):
    if N <= K:
        return 0

    sensor_list = list(set(sensor_list))
    sensor_list.sort()

    term_list = []
    for i in range(1, len(sensor_list)):
        term = sensor_list[i] - sensor_list[i-1]
        term_list.append(term)

    term_list.sort(reverse=True)
    term_list = term_list[K-1:]

    return sum(term_list)


print(solution(N, K, sensor_list))