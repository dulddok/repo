width = 0
height = 0
diag = 0

while True :
    trilist = list(map(int,input().split()))
    diag = max(trilist)

    trilist.remove(diag)

    width = trilist[0] ** 2
    height = trilist[1] ** 2
    diagonal = diag**2
    if width+height+diagonal== 0 :
        break
    if width+height == diagonal :
        print("right")
    elif width+height != diagonal :
        print('wrong')



