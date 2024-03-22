import sys
import heapq

def input():
    return sys.stdin.readline()

N = int(input())
pq_list = [list(map(int, input().split())) for _ in range(N)]

def solution():
    pq_list.sort()

    stack = [pq_list[0][1]]
    answer = [1]

    for P, Q in pq_list[1:]:
        flag = False
        for i ,end in enumerate(stack):
            if P > end:
                flag = True
                stack[i] = Q
                answer[i]+=1
                continue
        
        if not flag:
            stack.append(Q)
            answer.append(1)
    
    print(len(answer))
    print(*answer)


def solution2():
    pq_list.sort()

    pq = []
    computer_list = []

    for P, Q in pq_list:
        if not pq:
            heapq.heappush(pq, (Q, len(computer_list)))
            computer_list.append(1)

        else:
            if pq[0][0] < P:
                _, site = heapq.heappop(pq)
                heapq.heappush(pq, (Q, site))
                computer_list[site] += 1

            else:
                heapq.heappush(pq, (Q, len(computer_list)))
                computer_list.append(1)
                
    
    print(len(computer_list))
    print(*computer_list)

solution2()