from itertools import combinations_with_replacement
import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
a=[int(input()) for i in range(n)]

for i in a:
    t=[]
    z=0

    for j in range(1,i+1):
        if(j*(j+1))//2 > i :
            break
        t.append((j*(j+1))//2)

    com=list(combinations_with_replacement(t,3))

    for k in com :
        if sum(k) == i:
            z=1
            break
    print(z)