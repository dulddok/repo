N = int(input())
cnt = 0
sixtitle = 666

while True :
    if '666' in str(sixtitle) :
        cnt+=1
    if cnt == N :
        print(sixtitle)
        break
    sixtitle +=1
#sixtitle을 1씩 더해가는 while문을 만들어 666이 안에 들어있다면 cnt를 1 증가시키고 cnt가 N 과 같을 시 sixtitle 출력