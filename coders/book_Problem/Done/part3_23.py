N = int(input())


import heapq

hq = []

for _ in range(N):
    name, korean, english, math = input().split()
    heapq.heappush(hq, (-int(korean), int(english), -int(math), str(name)))

for i in range(N):
    print(heapq.heappop(hq)[-1])