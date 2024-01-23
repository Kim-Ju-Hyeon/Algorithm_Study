'''
https://www.acmicpc.net/problem/21611
'''

import sys

N, M = map(int, sys.stdin.readline().split())

grid = []
for _ in range(N):
    grid.append(list(map(int, sys.stdin.readline().split())))

skill = []
for _ in range(M):
    skill.append(list(map(int, sys.stdin.readline().split())))

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
temp = [3, 2, 4, 1]
n = int((N - 1) / 2)

answer_dict = {1: 0, 2: 0, 3: 0}
answer = 0

mid = int((N - 1) / 2)
for i in range(M):
    d_i, s_i = skill[i][0] - 1, skill[i][1]
    cur_r, cur_c = mid, mid
    for _ in range(s_i):
        new_r, new_c = cur_r + direction[d_i][0], cur_c + direction[d_i][1]
        grid[new_r][new_c] = None
        cur_r, cur_c = new_r, new_c

    array = []
    cur_r, cur_c = mid, mid
    for nn in range(1, n + 1):
        for i in range(4):
            nd = direction[temp[i] - 1]

            if i == 0 or i == 1:
                for _ in range(2 * nn - 1):
                    new_r, new_c = cur_r + nd[0], cur_c + nd[1]
                    cur_r, cur_c = new_r, new_c
                    if grid[cur_r][cur_c] is not None:
                        array.append(grid[cur_r][cur_c])
            else:
                for _ in range(2 * nn):
                    new_r, new_c = cur_r + nd[0], cur_c + nd[1]
                    cur_r, cur_c = new_r, new_c
                    if grid[cur_r][cur_c] is not None:
                        array.append(grid[cur_r][cur_c])

    nd = direction[2]
    for _ in range(2 * nn):
        new_r, new_c = cur_r + nd[0], cur_c + nd[1]
        cur_r, cur_c = new_r, new_c
        if grid[cur_r][cur_c] is not None:
            array.append(grid[cur_r][cur_c])

    while True:
        bomb_list = []
        i, j = 0, 1
        count = 0
        while j < len(array):
            if array[i] == array[j]:
                count += 1
            else:
                if count >= 3:
                    bomb_list.append([i, j - 1])
                if array[j] == 0:
                    break
                i = j
                count = 0
            j += 1

        if len(bomb_list) == 0:
            break
        else:
            for idx in range(len(bomb_list)):
                answer_dict[array[bomb_list[idx][0]]] += bomb_list[idx][1] - bomb_list[idx][0] + 1

                array[bomb_list[idx][0]:bomb_list[idx][1] + 1] = [None] * (bomb_list[idx][1] - bomb_list[idx][0] + 1)

            array = [num for num in array if num is not None]

    array = [num for num in array if num > 0]

    if len(array) > 0:
        new_array = []
        i, j = 0, 0
        count = 0
        while j < len(array):
            target = array[j]
            if array[i] == target:
                count += 1
                j += 1
                continue

            new_array += [count, array[i]]
            i = j
            count = 0

        new_array += [count, array[i]]
    else:
        new_array = []

    array = new_array[:N ** 2 - 1]
    if len(array) < N ** 2 - 1:
        array += [0] * (N ** 2 - 1 - len(array))

    grid = [[0] * N for _ in range(N)]
    point = 0
    cur_r, cur_c = mid, mid
    for nn in range(1, n + 1):
        for i in range(4):
            nd = direction[temp[i] - 1]

            if i == 0 or i == 1:
                for _ in range(2 * nn - 1):
                    new_r, new_c = cur_r + nd[0], cur_c + nd[1]
                    cur_r, cur_c = new_r, new_c
                    grid[cur_r][cur_c] = array[point]
                    point += 1
            else:
                for _ in range(2 * nn):
                    new_r, new_c = cur_r + nd[0], cur_c + nd[1]
                    cur_r, cur_c = new_r, new_c
                    grid[cur_r][cur_c] = array[point]
                    point += 1

    nd = direction[2]
    for _ in range(2 * nn):
        new_r, new_c = cur_r + nd[0], cur_c + nd[1]
        cur_r, cur_c = new_r, new_c
        grid[cur_r][cur_c] = array[point]
        point += 1

for num in answer_dict:
    answer += num * answer_dict[num]

print(answer)
