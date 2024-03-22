import sys


def input():
    return sys.stdin.readline()


N = int(input())
numbers = [int(input()) for _ in range(N)]

def solution():
    summation = sum(numbers)
    print(round(summation/N))

    numbers.sort()
    mid = numbers[N//2]
    print(mid)

    dict = {}
    for num in numbers:
        if num not in dict:
            dict[num] = 1
        else:
            dict[num] += 1

    tmp = sorted(dict, key=lambda x: dict[x], reverse=True)
    mod = tmp[0]
    if N > 1:
        second_mod = tmp[1]
        if dict[mod] == dict[second_mod]:
            mod = second_mod
    print(mod)

    print(numbers[-1] - numbers[0])

solution()