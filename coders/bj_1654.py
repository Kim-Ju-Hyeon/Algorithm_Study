import sys

def input():
    return sys.stdin.readline()


K, N = map(int, input().split())
lan_list = [int(input()) for _ in range(K)]


def check(mm):
    return N <= sum([l//mm for l in lan_list])

def solution():
    s, e = 0, max(lan_list)
    sol = -1

    while s <= e:
        m = (s + e) // 2

        if m == 0:
            m = 1

        if check(m):
            sol = m
            s = m+1

        else:
            e = m-1

    return sol

print(solution())