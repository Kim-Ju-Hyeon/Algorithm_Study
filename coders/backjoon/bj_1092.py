# import sys
#
# def input():
#     return sys.stdin.readline()
#
# N = int(input())
# max_weight = list(map(int, input().split()))
# M = int(input())
# box_weight = list(map(int, input().split()))
#
# def solution():
#     carry = [0] * N
#     max_weight.sort()
#     box_weight.sort()
#
#     if max_weight[-1] < box_weight[-1]:
#         return -1
#
#     sb = 0
#     for i, c in enumerate(max_weight):
#         left_box = len(box_weight[sb:])
#         left_craine = N - i
#
#         if left_box % left_craine == 0:
#             max_carry = int(left_box // left_craine)
#         else:
#             max_carry = int(left_box // left_craine) + 1
#
#         count = 0
#         for j in range(sb, M):
#             if c < box_weight[j]:
#                 carry[i] = count
#                 break
#
#             if count == max_carry:
#                 carry[i] = max_carry
#                 break
#
#             if j == M-1:
#                 carry[i] = count+1
#                 break
#
#             count += 1
#
#         sb += count
#
#     return max(carry)
#
# print(solution())


# maxheap으로 풀면 될 것 같음
import sys
import heapq

input = sys.stdin.readline

crane = int(input())
weights_c = list(map(int, input().split()))
weights_c.sort(reverse=True)

box = int(input())
weights_b = list(map(int, input().split()))
weights_boxes = []
for i in range(box):
    heapq.heappush(weights_boxes, -weights_b[i])

def solution():
    count = 0

    if weights_c[0] < weights_boxes[0]:
        print(-1)
        sys.exit()

    while len(weights_boxes) > 0:
        for i in range(crane):
            num = -heapq.heappop(weights_boxes)
            if weights_c[i] < num:
                heapq.heappush(weights_boxes, -num)
            if len(weights_boxes) == 0:
                return count

        count += 1


print(solution())

'''
10
2 5 5 5 7 7 11 17 20 20
8
15 15 17 18 18 20 20 20
'''
