import sys


def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    need = [int(readl()) for _ in range(N)]
    return N, M, need


sol = -1
# 입력 받는 부분
N, M, need = Input_Data()


# 여기서 부터 작성
def take_off(need, mid):
    count = 0
    money = 0
    for i, n in enumerate(need):
        if i == 0:
            money = mid
            money -= n
            count += 1
            continue

        if money - n < 0:
            money = mid
            money -= n
            count += 1
        else:
            money -= n

    return count


def solution():
    s = max(need)
    e = sum(need)

    while s <= e:
        mid = (s + e) // 2
        take_off_num = take_off(need, mid)

        if take_off_num > M:
            s = mid + 1
        else:
            e = mid - 1

    return mid

# 출력하는 부분
print(solution())
