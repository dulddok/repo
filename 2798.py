N,M = map(int,input().split())
bnumber = list(map(int,input().split()))
result = 0
for i in range(N) :
    for j in range(i+1,N):
        for k in range(j+1,N):
            if bnumber[i]+bnumber[j]+bnumber[k] > M :
                continue
            else :
                result = max(result,bnumber[i]+bnumber[j]+bnumber[k])
print(result)