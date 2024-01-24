import sys


def Input_Data():
    readl = sys.stdin.readline
    map_bingo = [list(map(int, readl().split())) for _ in range(5)]
    seq_bingo = []
    for _ in range(5):
        seq_bingo += list(map(int, readl().split()))
    return map_bingo, seq_bingo


sol = 0
# 입력받는 부분
map_bingo, seq_bingo = Input_Data()

# 여기서부터 작성
idx_list = [False] * 26
bingo_dict = {}
for i in range(5):
    for j in range(5):
        bingo_dict[map_bingo[i][j]] = 5 * i + j + 1


def get_num_bingo():
    count = 0

    # 1
    for i in range(1, 6):
        bingo = True
        for j in range(5):
            idx = i + 5 * j
            if not idx_list[idx]:
                bingo = False
                break
        if bingo:
            count += 1

    # 2
    for i in range(5):
        bingo = True
        for j in range(1, 6):
            idx = i * 5 + j
            if not idx_list[idx]:
                bingo = False
                break
        if bingo:
            count += 1

    # 3
    bingo = True
    for i in range(5):
        idx = 1 + i * 6
        if not idx_list[idx]:
            bingo = False
            break
    if bingo:
        count += 1

    # 4
    bingo = True
    for i in range(5):
        idx = 5 * (i + 1) - i
        if not idx_list[idx]:
            bingo = False
            break
    if bingo:
        count += 1

    return count


def solution():
    for ii, num in enumerate(seq_bingo):
        idx_list[bingo_dict[num]] = True
        if get_num_bingo() >= 3:
            return ii + 1


# 출력하는 부분
print(solution())
