# #7785
# import sys
# #input =sys.stdin.readline
# t = int(input())
# person={}
# for _ in range(t):
#     a,b = map(str, input().split())
#     if b=='enter': person[a]= 0
#     else : del person[a]
#
# person=sorted(person.keys(),reverse=True)
# print(*person, sep="\n")

import sys
input = sys.stdin.readline
n = int(input())
employee = {}

for i in range(n) :
    name, check = map(str,input().split())
    if check == 'enter' : employee[name] = check
    else :
        if employee[name] : del employee[name]

rs = sorted(employee.keys(),reverse=True)
print(rs)
