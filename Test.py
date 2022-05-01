# # 1부터 9까지의 수의 제곱 값을 포함하는 리스트
# array = [i*i for i in range(10)]
# print(array)
# x = '' # The string is declared 여러줄 입력
# for line in iter(input, x):
#     pass
# # 10줄의 입력을 받아 리스트로 저장하기
# N = list(input() for _ in range(10))
# print(N)
#1. 값 두 개를 입력받아 변수 a와 b에 저장 (띄어쓰기 구분)
# a, b = input().split() #문자열로
# a, b = map(int, input().split()) #정수형으로
# a, b = map(float, input().split()) #실수형으로
#
# #2. 1차원 배열 입력받기 = 정수형 리스트로 저장
# num_list = list(map(int, input().split())) #입력 : 1 2 3 /출력 : [1, 2, 3]
#
# #3. 문자열 여러줄 입력받기
# s_list = [input() for _ in range(n)] #예시로 n에 3넣어 3줄 입력받기(엔터로 구분)
#
# #4. 한 문자열(숫자ex.12345) 받아서 한 글자씩 나누어 더하기
# s = input()
# for i in range(len(s)):
# 	sum += int(s[i])  #문자열은 슬라이싱 가능!! + 문자열 형변환
#
# #5. 띄어쓰기 없이 정수 여러개 입력받아 2차원 배열로 저장하기
# two_d = [list(map(int, input())) for _ in range(n)] #예시는 4줄 입력받음
#
# #6. 열은 띄어쓰기로 행은 엔터로 구분하여 입력받아 2차원 배열 저장하기
# t_d = [list(map(int, input().split())) for _ in range(n)]#예시는 4줄. 4.-와 결과는 같다.
#
# i = 216
# str(i)
# a = type(str(i))
# print(a)

N = int(input())
array =[0]*99999
for i in range(N) :
    i = int(input())
    v = 5
    array.insert(i,v)
print(array[5])