num1 = int(input())
num2 = int(input())
num3 = int(input())

des = list(str(num1*num2*num3))

answer = [0,0,0,0,0,0,0,0,0,0]

for num in des:
    answer[int(num)] +=1

for answ in answer :
    print(answ)