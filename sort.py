from random import randint
import time

# 배열에 10000개의 정수를 삽입
array = []
for _ in range(10000):
    array.append(randint(1,100)) # 1부터 100사이의 랜덤 정수

# 선택 정렬 프로그램 성능 측정
start_time = time.time()

# 선택 정렬 프로그램 소스 코드
for i in range(len(array)):
    min_index = i
    for j in range(i+1,len(array)) :
        if array[min_index] > array[j]:
            min_index =j
    array[i], array[min_index] = array[min_index], array[i] # swap

end_time = time.time() #측정 종료
print("선택정렬 성능 측정 : ",end_time-start_time) #수행 시간 출력 