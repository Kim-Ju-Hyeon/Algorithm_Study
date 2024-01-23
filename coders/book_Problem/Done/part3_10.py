'''
자물쇠와 열쇠
https://school.programmers.co.kr/learn/courses/30/lessons/60059
'''


def rotation(key):
    M = len(key)

    new_key = [[0]] * M
    for c in range(M):
        temp = []
        for r in range(-1, -(M + 1), -1):
            temp.append(key[r][c])

        new_key[c] = temp

    return new_key


def solution(key, lock):
    M = len(key)
    N = len(lock)

    for _ in range(4):
        key = rotation(key)

        for r in range(M + N + 1):
            for c in range(M + N + 1):
                extend_map = [[-1] * M + lock[i - M] + [-1] * M
                              if M <= i < M + N else [-1] * (2 * M + N)
                              for i in range(2 * M + N)]

                for d in range(M):
                    extend_map[r + d][c:c + M] = [extend_map[r + d][c:c + M][idx] + key[d][idx] for idx in range(M)]

                check = True
                for d in range(N):
                    for dd in range(N):
                        if extend_map[M + d][M:M + N][dd] != 1:
                            check = False

                if check:
                    return True
    return False



def rotate_a_matrix_by_90_degree(a):
    n = len(a)
    m = len(a[0])

    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]

    return result

def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)

    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    for rotation in range(4):
        key = rotate_a_matrix_by_90_degree(key)
        for x in range(n * 2):
            for y in range(n * 2):

                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]

                if check(new_lock) == True:
                    return True

                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y+ j] -= key[i][j]
    return False
