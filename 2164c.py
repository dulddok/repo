from collections import deque

n = int(input())
dq = deque()

for i in range(1,n+1) :
    dq.append(i)

while (len(dq) >1) :
    dq.popleft() # 위 카드 버리고
    dq.append(dq.popleft()) # 제일 위카드 맨 아래에 뭍이고고

print(dq[0])