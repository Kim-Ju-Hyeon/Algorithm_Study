import sys


def Input_Data():
    readl = sys.stdin.readline
    N, C = map(int, readl().split())
    M = int(readl())
    info = [list(map(int, readl().split())) for _ in range(M)]
    return N, C, M, info


# 입력받는 부분
N, C, M, info = Input_Data()


# 여기서부터 작성
def solution1():
    info.sort(key=lambda x: (x[0], x[1], -x[2]))

    truck = [0] * (N + 1)
    off_boxes = [0] * (N + 1)

    prev_town = 1
    sol = 0
    for cur_town, off_town, boxes in info:
        if cur_town != prev_town:
            truck[cur_town] -= off_boxes[cur_town]
            off_boxes[cur_town] = 0

        on_boxes = min(boxes, C - truck[cur_town])
        sol += on_boxes

        for t in range(cur_town, off_town + 1):
            truck[t] += on_boxes
        off_boxes[off_town] += on_boxes

        prev_town = cur_town

    print(sol)

def solution2():
    info.sort(key=lambda x: (x[1], -x[0], x[2]))
    truck = [0] * (N+1)
    sol = 0

    for in_t, out_t, boxes in info:
        on_boxes = min(boxes, C - max(truck[in_t:out_t]))

        for t in range(in_t, out_t):
            truck[t] += on_boxes

        sol += on_boxes

    return sol

print(solution2())