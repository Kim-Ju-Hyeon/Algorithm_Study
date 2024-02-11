import sys

def input():
    return sys.stdin.readline()


N, M, L = map(int, input().split())
input_list = list(map(int, input().split()))

def solution(N,M,L,input_list):
    input_list.append(0)
    input_list.append(L)

    while M > 0:
        input_list.sort()
        term_list = []
        max_term, max_idx = -1, None

        for i in range(1, len(input_list)):
            term = input_list[i] - input_list[i-1]
            term_list.append(term)

            if term > max_term:
                max_term = term
                max_idx = i


        new_center = (input_list[max_idx] + input_list[max_idx-1]) // 2
        input_list.append(new_center)
        M -= 1


    input_list.sort()
    term_list = []

    for i in range(1, len(input_list)):
        term = input_list[i] - input_list[i - 1]
        term_list.append(term)

    return max(term_list)


def check(term_list, m):
    num_new = 0
    for term in term_list:
        if term >= m:
            if term % m == 0:
                num_new += (term // m) - 1
            else:
                num_new += term // m

    if M == num_new:
        return True
    elif M > num_new:
        return True
    else:
        return False

def solution2():
    input_list.append(0)
    input_list.append(L)
    input_list.sort()

    term_list = []
    for i in range(1, len(input_list)):
        term = input_list[i] - input_list[i - 1]
        term_list.append(term)

    s = 1
    e = max(term_list)
    answer = None
    while s <= e:
        m = (s+e) // 2
        print(s, e, m)
        print(check(term_list, m))
        if check(term_list, m):
            answer = m
            e = m - 1
        else:
            s = m + 1

    return answer


print(solution2())