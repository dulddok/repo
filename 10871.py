A,B = map(int,input().split())
Xlist = list(map(int,input().split()))
for i in range(A):
    if Xlist[i] < B :
        print(Xlist[i], end=" ")

