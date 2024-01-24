import sys


def Input_Data():
    readl = sys.stdin.readline
    N = int(readl())
    return N


sol = 0
# 입력받는 부분
N = Input_Data()

# 여기서부터 작성
def is_happy_num(num):
    _temp = {}
    while True:
        next_num = sum([int(nn) ** 2 for nn in str(num)])
        if next_num == 1:
            return True
        if next_num in _temp:
            return False
        else:
            _temp[next_num] = None
        num = next_num


ans = -1e99
for i in range(1, N + 1):
    if is_happy_num(i):
        ans = max(ans, i)

print(ans)