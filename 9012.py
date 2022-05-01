# t = int(input())
#
# for i in range(t):
#     ps = input()
#     bracket = []
#
#     for j in ps :
#         if j == '(' :
#             bracket.append(j)
#         elif j == ')':
#             if bracket:
#                 bracket.pop()
#             else :
#                 print('NO')
#                 break
#     else :
#         if not bracket:
#             print('YES')
#         else:
#             print('NO')
#


# T = int(input())
#
# for _ in range(T):
#     string = input()
#     stk = []
#     isVPS = True
#
#     for char in string:
#         if char == "(":
#             stk.append("(")
#         else: # char == ")"
#             if stk: # 스택이 비어있지 않으면
#                 stk.pop()
#             else: # 스택이 비어있다면, 닫힌 괄호가 많다
#                 isVPS = False
#                 break
#
#     if stk: # 스택이 비어있지 않으면, 열린 괄호가 많다
#         isVPS = False
#
#     if isVPS:
#         print("YES")
#     else:
#         print("NO")