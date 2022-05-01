T = int(input())
for i in range(T):
    N,M = map(int,input().split())
    cnt = 0
    for j in range(N,M+1) :
       zchk = str(j)
       cnt +=zchk.count('0')
    print(cnt)
