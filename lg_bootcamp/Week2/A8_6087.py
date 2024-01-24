import sys


def Input_data():
    readl = sys.stdin.readline
    N = int(input())
    return N


sol = 0

# 입력받는 부분
N = Input_data()


# 여기서부터 작성
def solution(N):
    count = 0
    power = len(str(N)) - 1
    count_list = [0] * power
    count_list[0] = 9

    for i in range(1, power):
        count_list[i] = 9 * count_list[i - 1]

    while N >= 10:
        pp = len(str(N)) - 1
        if int(str(N)[0]) == 1:
            count += count_list[pp - 1]
            N -= 10 ** pp
        else:
            for n in range(1, int(str(N)[0])):
                if n == 4:
                    continue
                count += count_list[pp - 1]

            N -= (10 ** pp) * (int(str(N)[0]) - 1)

    for nn in range(1, N + 1):
        if nn != 4:
            count += 1

    return count


print(solution(N))