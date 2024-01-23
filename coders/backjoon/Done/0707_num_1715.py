'''
https://www.acmicpc.net/problem/1715
'''

from heapq import heappop, heappush

N = int(input())

card_list = []
for _ in range(N):
    heappush(card_list, int(input()))

answer = 0
while len(card_list) > 1:
    min_card = heappop(card_list)
    sum_card = min_card + heappop(card_list)
    answer += sum_card
    heappush(card_list,sum_card)

print(answer)