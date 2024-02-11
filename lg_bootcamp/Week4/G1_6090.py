import sys


def Input_Data():
    N, B = map(int, readl().split())
    height = [int(readl()) for _ in range(N)]
    return N, B, height


readl = sys.stdin.readline
T = int(readl())
for _ in range(T):
    # 입력받는 부분
    N, B, height = Input_Data()

    # 여기서부터 작성
    answer = [1e99]


    def dfs_binary_tree(idx, cur_sum):
        if cur_sum >= B:
            answer[0] = min(answer[0], cur_sum - B)
            return

        if idx >= N:
            return

        dfs_binary_tree(idx + 1, cur_sum + height[idx])
        dfs_binary_tree(idx + 1, cur_sum)

    def dfs_comb(s, cur_sum):
        if cur_sum >= B:
            answer[0] = min(answer[0], cur_sum - B)
            return

        for i in range(s, N):
            dfs_comb(i+1, cur_sum+height[i])

    dfs_binary_tree(0, 0)

    print(answer[0])
