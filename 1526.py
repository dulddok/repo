n = int(input())

while True :
    cnt = 1
    for i in str(n):
        if i !='4' and i !='7':
            cnt = 0
            n -=1
    if cnt == 1 : print(n) ; break

