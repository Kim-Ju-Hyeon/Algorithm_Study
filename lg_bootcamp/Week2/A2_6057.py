import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    num = [int(readl()) for _ in range(N)]
    return N, num


sol = 0

# 입력받는 부분
N, num = Input_Data()


# 여기서부터 작성
def solution(number):
    while len(str(number)) > 1:
        number_str = str(number)
        number = sum([int(nn) for nn in number_str])
    return number


answer_list = []
for n in num:
    digit_root = solution(n)
    answer_list.append((digit_root, n))

answer_list.sort(key=lambda x: (x[0], -x[1]))

# 출력하는 부분
print(answer_list[-1][-1])