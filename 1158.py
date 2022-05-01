from collections import deque

n,k = map(int,input().split())

dqlist = deque([i for i in range(1,n+1)])
yosepus = []
idx = 0

while True :
    idx +=1
    if idx < k and dqlist :
        dqlist.append(dqlist.popleft())

    elif idx == k and dqlist :
        yosepus.append(dqlist.popleft())
        idx =0
    elif len(dqlist) < k :
        for dq in dqlist :
            yosepus.append(dq)
        break

print("<",end='')
yose = ''.join(str(yosepus)[1:-1])
print(yose,end='')
print(">")
