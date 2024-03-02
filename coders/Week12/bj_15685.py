import sys

def input():
    return sys.stdin.readline()


N = int(input())
curve_info = []
for _ in range(N):
    curve_info.append(list(map(int, input().split())))

def solution():
    # 맵 초기화
    grid = [[0]*101 for _ in range(101)]

    # 4방향 움직임 정의
    direction = [(0, 1), (-1, 0), (0, -1), (1, 0)]

    # 맨 끝 자리 기준으로 시계 방향 90도 회전 함수
    def rotate_90(_dragon_curve):
        y, x = _dragon_curve[-1]
        for ny, nx in _dragon_curve[::-1][1:]:
            dy = ny - y
            dx = nx - x

            if dy <= 0 and dx <= 0:
                ry = y - abs(dx)
                rx = x + abs(dy)

            elif dy <= 0 and dx >= 0:
                ry = y + abs(dx)
                rx = x + abs(dy)

            elif dy >= 0 and dx >= 0:
                ry = y + abs(dx)
                rx = x - abs(dy)

            else:
                ry = y - abs(dx)
                rx = x - abs(dy)

            _dragon_curve.append((ry, rx))

        return _dragon_curve

    dragon_curve_loc = []
    for start_x, start_y, d, g in curve_info:
        # 0번째 
        dragon_curve = [(start_y, start_x), (start_y + direction[d][0], start_x + direction[d][1])]

        for _ in range(g):
            dragon_curve = rotate_90(dragon_curve)

        dragon_curve_loc += dragon_curve
    
    # check dragon curve
    dragon_curve_loc = list(set(dragon_curve_loc))
    for y, x in dragon_curve_loc:
        if 0 <= y <= 100 and 0 <= x <= 100:
            grid[y][x] = 1

    
    box_d = [[(-1, -1), (-1, 0), (0, -1)], [(-1, 0), (-1, 1), (0, 1)], [(0, -1), (1, -1), (1, 0)], [(0, 1), (1, 1), (1, 0)]]
    box = 0
    for y in range(101):
        for x in range(101):
            # (x,y)를 중심으로 4 방향 가능성 확인
            if grid[y][x] == 1:
                for i in range(4):
                    flag = True
                    # 3 방향 check
                    for j in range(3):
                        ny = y + box_d[i][j][0]
                        nx = x + box_d[i][j][1]

                        if 0 <= ny <= 100 and 0 <= nx <= 100:
                            if grid[ny][nx] == 0:
                                flag = False
                        else:
                            flag = False
                    if flag:
                        box += 1

    return box // 4


print(solution())