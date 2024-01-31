import sys
from collections import deque


def Input_Data():
    readl = sys.stdin.readline
    S, E = map(int, readl().split())
    return S, E


# 입력받는 부분
S, E = Input_Data()


# 여기서부터 작성
def is_prime(n):
    if n % 2 == 0:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def check2(num_i, num_j):
    num_i, num_j = str(num_i), str(num_j)
    count = 0

    for idx in range(4):
        if num_i[idx] != num_j[idx]:
            count += 1

    if count == 1:
        return True
    else:
        return False


def solution(S, E):
    num = min(S, E)
    num_list = []

    while num <= max(S, E):
        if is_prime(num):
            num_list.append(num)
        num += 1

    visited = [False] * 10000
    q = deque()
    q.append((S, 0))
    visited[S] = True

    while q:
        cur_station, cur_dist = q.popleft()

        if cur_station == E:
            return cur_dist

        for next_station in num_list:
            if not visited[next_station] and check2(cur_station, next_station):
                q.append((next_station, cur_dist + 1))
                visited[next_station] = True


def change_digit(num):
    num_str = str(num)
    changed_nums = set()

    for i in range(4):  # 네 자리 숫자의 각 자리를 반복
        for d in range(10):  # 0부터 9까지의 숫자로 바꾸기
            if num_str[i] == str(d):  # 같은 숫자는 제외
                continue
            if i == 0 and d == 0:  # 첫 번째 자리를 0으로 만드는 것은 제외
                continue

            # 숫자 변경
            new_num = num_str[:i] + str(d) + num_str[i+1:]

            # 변경된 숫자를 집합에 추가
            changed_nums.add(int(new_num))
    changed_nums = list(changed_nums)
    return changed_nums


def solution2(S, E):
    visited = [False] * 10000
    q = deque()
    q.append((S, 0))
    visited[S] = True

    while q:
        cur_station, cur_dist = q.popleft()
        if cur_station == E:
            return cur_dist

        for next_station in change_digit(cur_station):
            if not visited[next_station] and is_prime(next_station):
                q.append((next_station, cur_dist+1))
                visited[next_station] = True


print(solution2(S, E))
