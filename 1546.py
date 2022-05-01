N = int(input())
arr = list(map(int,input().split()))
avesum = 0

for arlist in arr :
    avesum += (arlist/max(arr))*100

print(avesum/N)