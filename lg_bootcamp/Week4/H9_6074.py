import sys

def input_data():
    readl = sys.stdin.readline
    W, H = map(int, readl().split())
    N = int(readl())
    info = [list(map(int, readl().split())) for _ in range(N+1)]
    return N, W, H, info

sol = -1

# 입력받는 부분
N, W, H, info = input_data()

# 여기서부터 작성
def solution():
    answer = 0
    return answer

# 출력하는 부분
print(solution())