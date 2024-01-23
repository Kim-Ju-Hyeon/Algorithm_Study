# 큰 수의 법칙

# Input: N,M,K
# Output: int

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
i = 0
answer = 0

for i in range(m):
    if (i+1) % (k+1) == 0:
        answer += data[-2]
    else:
        answer += data[-1]

print(answer)


### 답안 예시
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)