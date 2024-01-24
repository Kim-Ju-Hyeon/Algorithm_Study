import sys


def Input_Data():
    readl = sys.stdin.readline
    K = int(readl())
    N = int(readl())
    info = [readl().split() for _ in range(N)]
    info = [(int(t), z) for t, z in info]
    return K, N, info


# 입력받는 부분
K, N, info = Input_Data()


# 여기서부터 작성
def sol(K):
    T = 0

    for quiz_time in info:
        t, z = quiz_time
        T += t
        if T > 210:
            return K

        if z == 'T':
            if K < 8:
                K += 1
            elif K == 8:
                K = 1

print(sol(K))

'''
3
5
20 T
50 T
80 T
50 T
30 T
'''
