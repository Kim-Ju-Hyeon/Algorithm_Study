import sys

def input():
    return sys.stdin.readline()

N = int(input())

input_list = []
for _ in range(N):
    input_list.append(int(input()))

input_list.sort()
answer = [abs(n - (i+1)) for i, n in enumerate(input_list)]

print(sum(answer))