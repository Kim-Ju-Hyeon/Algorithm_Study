import sys


def input_data():
    readl = sys.stdin.readline
    N, P = map(int, readl().split())
    return N, P


sol = 0

# 입력받는 부분
N, P = input_data()


# 여기서부터 작성
idx = 0
hash = {N: idx}

prev_N = N
while True:
    Next_N = (prev_N * N) % P
    idx += 1

    if Next_N in hash:
        answer = idx - hash[Next_N]
        break
    else:
        hash[Next_N] = idx
    prev_N = Next_N

print(answer)
