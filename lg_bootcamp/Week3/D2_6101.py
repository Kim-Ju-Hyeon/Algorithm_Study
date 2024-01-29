import sys


def Input_Data():
    readl = sys.stdin.readline
    N, K = map(int, readl().split())
    num = readl().strip()
    return N, K, num


sol = -1
# 입력받는 부분
N, K, num = Input_Data()

# 여기서부터 작성
def solution(K, num):
    stack = []

    for n in num:
        while len(stack) and K > 0 and stack[-1] < n:
            stack.pop()
            K -= 1
        stack.append(n)




# 출력하는 부분
print(solution())