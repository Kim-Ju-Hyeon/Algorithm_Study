import sys


def input_data():
    map_soli = [[0] + list(readl().strip()) + [0] if 1 <= r <= 5 else [0] * 11 for r in range(7)]
    readl()
    return map_soli


readl = sys.stdin.readline
T = int(readl())
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for _ in range(T):
    # 입력받는 부분
    map_soli = input_data()

    total_pin = 0
    for row in range(1, 6):
        for col in range(1, 10):
            if map_soli[row][col] == 'o':
                total_pin += 1

    answer = [-1e99]


    def dfs(num_move, pins):
        answer[0] = max(num_move, answer[0])

        if num_move > answer[0]:
            return False

        for row in range(1, 6):
            for col in range(1, 10):
                if map_soli[row][col] == 'o':
                    for dr, dc in move:
                        nr = row + dr
                        nc = col + dc

                        nnr = nr + dr
                        nnc = nc + dc

                        if map_soli[nr][nc] == 'o' and map_soli[nnr][nnc] == '.':
                            map_soli[row][col] = '.'
                            map_soli[nnr][nnc] = 'o'
                            map_soli[nr][nc] = '.'

                            dfs(num_move + 1, pins-1)

                            map_soli[row][col] = 'o'
                            map_soli[nnr][nnc] = '.'
                            map_soli[nr][nc] = 'o'

        return False

    dfs(0, total_pin)
    print(total_pin - answer[0], answer[0])