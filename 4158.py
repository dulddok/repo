# import sys
# input = sys.stdin.readline

# while True:
#     n, m = map(int, input().split())
#
#     if n == 0 and m == 0:
#         break
#
#     s = set()
#     for _ in range(n):
#         CD = int(input())
#         s.add(CD)
#     ans = 0
#     for _ in range(m):
#         CD = int(input())
#         if CD in s:
#             ans += 1
#
#     print(ans)


while True :
    sang, sun = map(int,input().split())
    if sang ==0 and sun ==0 :
        break

    s = set()
    for i in range(sang) :
        cd = int(input())
        s.add(cd)
    cnt = 0
    for j in range(sun):
        cd = int(input())
        if cd in s :
            cnt+=1

    print(cnt)

