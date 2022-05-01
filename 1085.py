recArr = list(map(int,input().split()))

leastx = 0
leasty = 0

if recArr[0] > recArr[2]-recArr[0] :
    leastx = recArr[2]-recArr[0]

elif recArr[0] < recArr[2]-recArr[0] :
    leastx = recArr[0]

if recArr[1] > recArr[3] - recArr[1] :
    leasty = recArr[3] - recArr[1]
elif recArr[1] < recArr[3] - recArr[1] :
    leasty = recArr[1]

if leastx < 0 or leasty <0 :

least = min(leastx,leasty)
if least < 0 :
    print(least*-1)
else :
    print(least)