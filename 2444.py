N = int(input())
space = ' '
for i in range(1,N+1):
    print(space*(N-i)+'*'* (2*i-1))
for j in range(N-1,0,-1) :
    print(space*(N-j)+'*'*(2*j-1))