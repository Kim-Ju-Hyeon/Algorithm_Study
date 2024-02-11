import sys
from bisect import bisect_left, bisect_right


def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	pos = [int(readl()) for _ in range(N)]
	return N, pos


sol = -1
# 입력받는 부분
N, pos = Input_Data()

# 여기서부터 작성
pos.sort()

for i in range(N-2):
	for j in range(i, N-1):
		range_start = pos[j] + (pos[j] - pos[i])
		range_end = pos[j] + 2*(pos[j] - pos[i])

		k = bisect_left(pos, range_start)
		if k == N or pos[k] > range_end:
			continue



# 출력하는 부분
print(sol)