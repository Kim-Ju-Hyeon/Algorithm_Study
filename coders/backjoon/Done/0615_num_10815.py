# https://www.acmicpc.net/problem/10815
# 숫자 카드

'''
문제
숫자 카드는 정수 하나가 적혀져 있는 카드이다.
상근이는 숫자 카드 N개를 가지고 있다.
정수 M개가 주어졌을 때,
이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.
'''

import sys


def binary_search(array, target, start, end):
    if start > end:
        return False
    mid = (start+end)//2
    if array[mid] == target:
        return True
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)


N = int(input())
card_list = list(map(int, sys.stdin.readline().split()))

M = int(input())
check_list = list(map(int, sys.stdin.readline().split()))


card_list.sort()

for c in check_list:
    if binary_search(card_list, c, 0, N - 1):
        print(1, end=' ')
    else:
        print(0, end=' ')

