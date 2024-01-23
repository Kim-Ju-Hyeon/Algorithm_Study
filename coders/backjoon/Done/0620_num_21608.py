'''
https://www.acmicpc.net/problem/21608
'''

import heapq

N = int(input())

preference_seat = []
for _ in range(N**2):
    preference_seat.append(list(map(int, input().split())))

class_room = [[0] * N for _ in range(N)]

d = [[0, 1], [0, -1], [1, 0], [-1, 0]]

student_preference_dict = {}
for student_seat_list in preference_seat:
    student = student_seat_list[0]
    preference_list = student_seat_list[1:]
    student_preference_dict[student] = preference_list

    q = []
    for row in range(N):
        for col in range(N):
            if class_room[row][col] == 0:
                like = 0
                blank = 0
                for i in range(4):
                    nrow, ncol = row + d[i][0], col + d[i][1]
                    if 0 <= nrow < N and 0 <= ncol < N:
                        if class_room[nrow][ncol] in preference_list:
                            like += 1
                        if class_room[nrow][ncol] == 0:
                            blank += 1
                if like > 0:
                    like *= -1
                if blank > 0:
                    blank *= -1

                heapq.heappush(q, (like, blank, row, col))
    _, _, min_row, min_col = heapq.heappop(q)
    class_room[min_row][min_col] = student

total_score = 0
for row in range(N):
    for col in range(N):
        stu = class_room[row][col]
        stu_prefer = student_preference_dict[stu]
        count = 0
        for i in range(4):
            nrow, ncol = row + d[i][0], col + d[i][1]
            if 0 <= nrow < N and 0 <= ncol < N:
                if class_room[nrow][ncol] in stu_prefer:
                    count += 1

        if count == 0:
            total_score += 0
        elif count == 1:
            total_score += 1
        elif count == 2:
            total_score += 10
        elif count == 3:
            total_score += 100
        else:
            total_score += 1000

print(total_score)