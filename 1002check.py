import math
N = int(input())
for i in range(0,N) :
    x1,y1,r1,x2,y2,r2 =list(map(int,input().split()))
    distance = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if distance == 0 and r1==r2 : # 두 원이 동심원이고 반지금 같을 때
        print(-1)
    elif abs(r1-r2) == distance or r1+r2 ==distance : # 내접 외접 일때
        print(1)
    elif abs(r1-r2) <distance<(r1+r2): # 두 원이 서로다른 두 점에서 만날때
        print(2)
    else :
        print(0) # 그 외에


## abs - 절대값 구하는 함수
'''
여기서 r1 r2는 원의 반지름입니다. 
반지름의 길이가 r1인 원과 r2인 원의 중심거리를 d라고 할 때,  |r1 - r2| 또는 r1 + r2와의 크기를 비교하면, 두 원의 위치 관계를 알 수 있다.
r1 + r2 < d 이면 두 원은 서로의 외부에 위치한다.
r1 + r2 = d 이면 두 원은 외접한다.
|r1 - r2| < d < r1 + r2 이면 두 원은 서로 다른 두 점에서 만난다.
|r1 - r2| = d 이면 한 원이 다른 원에 내접한다.
|r1 - r2| > d, r1 ≠ r2 이면 한 원이 다른 원의 내부에 있다.
'''