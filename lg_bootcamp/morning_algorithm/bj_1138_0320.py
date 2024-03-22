import sys

def input():
    return sys.stdin.readline()


N = int(input())
order = list(map(int, input().split()))

def solution():
    answer = [0]*(N+1)
    i = N
    for n in order[::-1]:
        i -= 1
        pass

solution()