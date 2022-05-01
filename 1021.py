from collections import deque


n, fnumber = map(int,input().split())
qlist = map(int,input().split())


dqlist = deque([i for i in range(1,n+1)])

qcount =0

for q in qlist:
    while True :
        if q == dqlist[0] :
            dqlist.popleft()
            break
        else :
            if dqlist.index(q) > len(dqlist)/2 :
                dqlist.appendleft(dqlist.pop())
                qcount+=1
            else :
                dqlist.append(dqlist.popleft())
                qcount += 1
print(qcount)
