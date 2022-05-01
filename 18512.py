x, y , p1, p2 = map(int,input().split())

xmove =[p1]
ymove=[p2]
answer = -1
cnt = 1
while (True):
    p1+=x
    p2+=y
    xmove.append(p1)
    ymove.append(p2)
    if p1 in ymove or p2 in xmove:
        answer= min(p1,p2)
        break
    elif cnt > 1000 :
        break
    cnt+=1
print(answer)