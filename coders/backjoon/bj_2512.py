import sys

def input():
    return sys.stdin.readline()


N = int(input())
budget_list = list(map(int, input().split()))
max_budget = int(input())

def check(mm):
    total = 0
    for money in budget_list:
       if money < mm:
           total += money
       else:
           total += mm

    return total <= max_budget

def solution():
    s, e = 0, max(budget_list)
    answer = -1

    while s <= e:
        m = (s + e) // 2

        # 예산 배정 가능
        if check(m):
            answer = m
            s = m+1
        else:
            e = m-1
    return answer

print(solution())