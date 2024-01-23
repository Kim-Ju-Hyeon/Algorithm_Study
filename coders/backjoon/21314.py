import sys

def input():
    return sys.stdin.readline()

# minkum_num -> str type
minkyum_num = input()

def solution(minkyum_num):
    print(minkyum_num.split('K'))

print(solution(minkyum_num))
