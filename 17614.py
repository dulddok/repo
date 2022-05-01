# N = int(input())
#
# cnt = 0
# for i in range(N+1) :
#     cnt +=str(i).count('3')+str(i).count('6')+str(i).count('9')
#
# print(cnt)

# N = int(input())
# clapcount = 0
#
# for i in range(N+1) :
#     number = i
#     while number !=0 :
#         n = number % 10
#         if n ==3 or n ==6 or n ==9 :
#             clapcount +=1
#         number = number//10
#
#
# print(clapcount)




N = int(input())
cnt = 0

for i in range(1,N+1):
    num = i
    while num !=0 :
        n = num % 10
        if n == 3 or n == 6 or n==9 :
            cnt +=1
        num = num //10
print(cnt)