while True :
    a = int(input())
    print("==========구구단 시작===========")
    if a < 10 :
        for i in range(2,10):
            print(a, "*", i,'=',a*i)
            continue
    else :
        print("입력 값이 너무 큽니다.")
        break
