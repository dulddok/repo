A,B = map(int,input().split())
Res=[]
Numlist = list(map(int,input().split(',')))

for i in range(B) :
    for j in range(len(Numlist)-1) :
        Res.append(Numlist[j+1] - Numlist[j])
    Numlist = Res
    Res = []

Numlist = list(map(str,Numlist))
print(','.join(Numlist))

## join 함수는 구분자.join(리스트)
# .join 을 이용하면 매개변수로 들어온  Numlist 의 배열 값들을
#Numlist1Numlist2 이런식ㅇ으로 나오게하고 앞에 구분자로 나눠줌

