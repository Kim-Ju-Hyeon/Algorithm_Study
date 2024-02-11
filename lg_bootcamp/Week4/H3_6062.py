import sys


def Input_Data():
	readl = sys.stdin.readline
	W = int(readl())
	cnt = list(map(int,readl().split()))
	return W, cnt


sol, sol_cnt = -1, [0] * 6
# 입력받는 부분
W, cnt = Input_Data()

# 여기서부터 부분
def solution(W, cnt):
	cnt = cnt[::-1]
	coin = [1, 5, 10, 50, 100, 500, 1000]

	for idx in range(6):
		count = cnt[idx]
		while True:
			if W <= 0:
				return

			if count <= 0:
				sol_cnt[idx] = 0
				break

			check_w = W - coin[idx] * count
			if check_w >= 0 and check_w % coin[idx + 1] == 0:
				break
			else: count -= 1

		sol_cnt[idx] = count
		W -= coin[idx] * sol_cnt[idx]


solution(W, cnt)
# 출력하는 부분
print(sum(sol_cnt))
print(*sol_cnt[::-1])