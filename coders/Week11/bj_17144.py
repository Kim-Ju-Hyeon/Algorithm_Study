import sys

def input():
    return sys.stdin.readline()

R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]


def solution():
    global room

    air_cleaner = []
    for row in range(R):
        if room[row][0] == -1:
            air_cleaner.append(row)

    def diffusion(_room):
        new_room = [[0]*C for _ in range(R)]
        for loc in air_cleaner:
            new_room[loc][0] = -1

        dr = [0, 0, 1, -1]
        dc = [1, -1, 0, 0]

        for row in range(R):
            for col in range(C):
                if _room[row][col] != 0 and _room[row][col] != -1:
                    dust = _room[row][col] // 5
                    count = 0
                    for i in range(4):
                        nr = row + dr[i]
                        nc = col + dc[i]

                        if 0 <= nr < R and 0 <= nc < C and _room[nr][nc] != -1:
                            new_room[nr][nc] += dust
                            count += 1

                    new_room[row][col] += _room[row][col] - dust * count

        return new_room

    def cleaning(_room):
        # 반 시계 방향 회정 - 공기 청정기 윗 부분
        r = air_cleaner[0]
        # 오른쪽
        prev = 0
        for col in range(1, C):
            temp = _room[r][col]
            _room[r][col] = prev
            prev = temp

        # 윗 쪽
        for row in range(r-1, -1, -1):
            temp = _room[row][C-1]
            _room[row][C-1] = prev
            prev = temp

        # 왼쪽
        for col in range(C-2, -1, -1):
            temp = _room[0][col]
            _room[0][col] = prev
            prev = temp

        # 아래
        for row in range(1, r):
            temp = _room[row][0]
            _room[row][0] = prev
            prev = temp

        # 시계 방향 회정 - 공기 청정기 아랫 부분
        r = air_cleaner[1]

        # 오른쪽
        prev = 0
        for col in range(1, C):
            temp = _room[r][col]
            _room[r][col] = prev
            prev = temp

        # 아래
        for row in range(r+1, R):
            temp = _room[row][C-1]
            _room[row][C-1] = prev
            prev = temp

        # 왼쪽
        for col in range(C-2, -1, -1):
            temp = _room[R-1][col]
            _room[R-1][col] = prev
            prev = temp

        # 윗 쪽
        for row in range(R - 2, r, -1):
            temp = _room[row][0]
            _room[row][0] = prev
            prev = temp

        return _room


    for _ in range(T):
        new_room = diffusion(room)
        new_room = cleaning(new_room)
        room = new_room

    total = 0
    for r in range(R):
        total += sum(room[r])

    total += 2

    return total

print(solution())