import sys


def input():
    return sys.stdin.readline()


N, K = map(int, input().split())
S_k = list(map(int, input().split()))
D = list(map(int, input().split()))

def solution():
    global S_k
    for _ in range(K):
        prev_D = [0] * N

        for i in range(N):
            d_i = D[i]
            prev_D[d_i-1] = S_k[i]

        S_k = prev_D

    return S_k

print(*solution())
