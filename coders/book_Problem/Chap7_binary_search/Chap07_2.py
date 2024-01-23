import sys

N = int(input())
sell_list = list(map(int, sys.stdin.readline().split()))

M = int(input())
buy_list = list(map(int, sys.stdin.readline().split()))


def binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return True
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, start)

sell_list.sort()

for buy in buy_list:
    if binary_search(sell_list, buy, 0, N-1):
        print(1, end=" ")
    else:
        print(0, end=" ")