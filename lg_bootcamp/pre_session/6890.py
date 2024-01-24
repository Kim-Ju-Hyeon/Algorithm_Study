import sys


def Input_Data():
    N, K = map(int, readl().split())
    num = list(map(int, readl().split()))
    return N, K, num


sol = []
# 입력 받는 부분
readl = sys.stdin.readline

# 여기서부터 입력


T = int(readl())
for _ in range(T):
    N, K, num = Input_Data()
    num.sort()
    

# 출력하는 부분
print(*sol, sep='\n')
