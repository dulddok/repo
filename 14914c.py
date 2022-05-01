# apple, banana = map(int,input().split())
# person=1
# criteria = 0
# while True:
#     if apple % person == 0 and banana % person ==0 :
#         print(person,apple//person,banana//person)
#         # if apple // person == 1 or banana // person == 1 :
#         #     print(person, apple // person, banana // person)
#         #     criteria =1
#         if apple // person == 1 or banana // person == 1:
#             # print(person, apple // person, banana // person)
#             break
#
#     # if apple ==person  or banana == person :
#     #     print(person,apple//person,banana//person)
#     #     continue
#     person +=1
#
# def GCD(a,b) :
#     if max(a,b) % min(a,b) :
#         return GCD(max(a,b)%min(a,b),min(a,b))
#     else :
#         return min(a,b)
# a,b = map(int,input().split())
# for i in range(1,GCD(a,b)+1) :
#     if GCD(a,b) % i == 0 :
#         print(i,a//i,b//i)
from math import gcd

a,b = map(int,input().split())
g = gcd(a,b)
for i in range(1,g+1) :
    if g%i==0 :
        print(i,a//i,b//i)