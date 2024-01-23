'''
https://www.acmicpc.net/problem/14891
'''


import sys

def input():
    return sys.stdin.readline()


def rotate(arr, direction):
    new_arr = ''
    if direction == 1:
        new_arr += arr[-1]
        new_arr += arr[:7]
    else:
        new_arr += arr[1:]
        new_arr += arr[0]
    return new_arr


def check_left_gear(num, direction):
    if num - 1 < 0:
        return

    if gear_list[num][6] != gear_list[num - 1][2]:
        check_left_gear(num - 1, direction * -1)
        gear_list[num - 1] = rotate(gear_list[num - 1], direction * -1)
    else:
        return


def check_right_gear(num, direction):
    if num + 1 > 3:
        return

    if gear_list[num][2] != gear_list[num + 1][6]:
        check_right_gear(num + 1, direction * -1)
        gear_list[num + 1] = rotate(gear_list[num + 1], direction * -1)
    else:
        return


gear_list = []
for _ in range(4):
    temp = input().split()
    gear_list.append(temp[0])

K = int(input())
rotate_list = []
for _ in range(K):
    rotate_list.append(list(map(int, input().split())))

for N, d in rotate_list:
    check_left_gear(N-1, d)
    check_right_gear(N-1, d)
    gear_list[N - 1] = rotate(gear_list[N - 1], d)

answer = 0
for n in range(4):
    if gear_list[n][0] == '1':
        answer += 2 ** n

print(answer)
