T = int(input())

for i in range(T):
    h,w,p = list(map(int,input().split()))

    num = p//h+1
    floor = p%h
    if p%h ==0 : ## 투숙객의 수가 height의 배수일때
        num = p//h
        floor = h
    print(f'{floor*100+num}')

